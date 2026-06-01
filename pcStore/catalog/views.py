# catalog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Exists, OuterRef, Value, BooleanField, Count, Avg, Prefetch
from catalog.models import Product, Category, Review, ReviewAttachment, ReviewVote, ReviewComment, ProductImage
from cart.models import CartItem, Favorite
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import default_storage
from django.conf import settings
from .filters_config import FILTERS_CONFIG
from django.db.models.functions import Coalesce

import json

ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png', 'video/mp4']
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 МБ


def apply_filters(queryset, request, category_slug=None):
    """
    Объединяет общие фильтры (цена, бренд, наличие, сортировка)
    и динамические JSON-фильтры для конкретной категории.
    Поддерживает множественный выбор для чекбоксов.
    """
    # === 1. ОБЩИЕ ФИЛЬТРЫ ===
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_min.isdigit():
        queryset = queryset.filter(price__gte=int(price_min))
    if price_max and price_max.isdigit():
        queryset = queryset.filter(price__lte=int(price_max))

    # 🔥 Бренд теперь поддерживает множественный выбор
    brands = request.GET.getlist('brand')
    if brands:
        queryset = queryset.filter(brand__in=brands)

    if request.GET.get('in_stock') == '1':
        queryset = queryset.filter(in_stock__gt=0)

    # === 2. ДИНАМИЧЕСКИЕ ФИЛЬТРЫ ===
    if category_slug and category_slug in FILTERS_CONFIG:
        specs_config = FILTERS_CONFIG[category_slug]

        for key, spec in specs_config.items():
            # Пропускаем 'brand', он уже обработан выше
            if key == 'brand':
                continue

            # 🔹 Выпадающие списки (теперь с поддержкой множественного выбора)
            if spec['type'] == 'select':
                values = request.GET.getlist(key)
                if values:
                    # Используем OR-логику: товар подходит, если хотя бы одно значение совпадает
                    q_filter = Q()
                    for value in values:
                        q_filter |= Q(specifications__contains={key: value})
                    queryset = queryset.filter(q_filter)

            # 🔹 Чекбоксы (одиночные)
            elif spec['type'] == 'checkbox':
                value = request.GET.get(key)
                if value == '1':
                    queryset = queryset.filter(specifications__contains={key: True})

            # 🔹 Диапазоны (частоты, TDP и т.д.)
            elif spec['type'] == 'range':
                min_val = request.GET.get(f'{key}_min')
                max_val = request.GET.get(f'{key}_max')

                if min_val or max_val:
                    try:
                        min_f = float(min_val) if min_val else None
                        max_f = float(max_val) if max_val else None

                        if min_f is not None:
                            queryset = queryset.filter(**{f'specifications__{key}__gte': min_f})
                        if max_f is not None:
                            queryset = queryset.filter(**{f'specifications__{key}__lte': max_f})
                    except ValueError:
                        pass

    return queryset


def category_view(request, category_slug):
    """Отображение товаров категории с динамическими фильтрами (стиль DNS)"""
    category = get_object_or_404(Category, slug=category_slug)

    # 🔥 Базовый запрос
    products = Product.objects.filter(categories=category, is_active=True).distinct()

    # 🔥 Применяем фильтры
    products = apply_filters(products, request, category_slug)

    # 🔥 Добавляем аннотации ДЛЯ КАРТОЧЕК (после фильтров, до пагинации)
    products = products.annotate(
        reviews_count=Count('catalog_reviews'),
        avg_rating=Avg('catalog_reviews__rating'),
        is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
        is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
    ).prefetch_related('images')

    sort = request.GET.get('sort', 'popular')

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'new':
        products = products.order_by('-created_at')
    elif sort == 'rating':
        products = products.order_by(
            Coalesce('avg_rating', 0).desc(),
            '-reviews_count',
            '-views'
        )
    elif sort == 'reviews':
        products = products.order_by(
            '-reviews_count',
            Coalesce('avg_rating', 0).desc(),
            '-views'
        )
    else:  # 'popular' или по умолчанию
        products = products.order_by('-views')

    #  Формируем конфигурацию фильтров для шаблона
    config = {**FILTERS_CONFIG.get('_common', {}), **FILTERS_CONFIG.get(category_slug, {})}

    # Базовые товары для подсчёта (без применения фильтров, только категория)
    base_products = Product.objects.filter(categories=category, is_active=True).distinct()

    filters = {}
    for key, spec in config.items():
        # Получаем все выбранные значения (для множественного выбора)
        selected_values = request.GET.getlist(key)

        filter_data = {
            **spec,
            'value': request.GET.get(key),  # Для обратной совместимости
            'selected_values': selected_values,  # Список выбранных значений
            'current_min': request.GET.get(f'{key}_min', ''),
            'current_max': request.GET.get(f'{key}_max', ''),
        }

        # 🔥 Для select-фильтров считаем количество товаров по каждому значению
        if spec['type'] == 'select':
            counts = {}
            for option in spec.get('options', []):
                counts[option] = base_products.filter(
                    specifications__contains={key: option}
                ).count()
            filter_data['counts'] = counts

            # Для брендов — отдельная логика (поле brand, не specifications)
            if key == 'brand':
                counts = {}
                brands = base_products.filter(
                    brand__isnull=False
                ).exclude(brand='').values('brand').annotate(
                    count=Count('id')
                ).order_by('brand')

                for b in brands:
                    counts[b['brand']] = b['count']

                filter_data['options'] = [b['brand'] for b in brands]
                filter_data['counts'] = counts

        filters[key] = filter_data

    # 🔥 Пагинация
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'products': products_page,
        'filters': filters,
        'filter_params': filter_params.urlencode(),
    })


def product_detail(request, slug):
    """Детальная страница товара"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    product.increment_views()

    reviews = product.catalog_reviews.select_related('user').annotate(
        likes_count=Count('votes', filter=Q(votes__vote=1)),
        dislikes_count=Count('votes', filter=Q(votes__vote=-1))
    )

    if request.user.is_authenticated:
        user_votes = ReviewVote.objects.filter(
            review__in=reviews,
            user=request.user
        ).values('review_id', 'vote')
        votes_dict = {v['review_id']: v['vote'] for v in user_votes}
    else:
        votes_dict = {}

    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    # 🔥 Расчет распределения оценок
    rating_dist = []
    total_reviews = reviews.count()
    for i in range(5, 0, -1):
        count = reviews.filter(rating=i).count()
        percent = (count * 100) // total_reviews if total_reviews > 0 else 0
        rating_dist.append({'rating': i, 'count': count, 'percent': percent})

    # 🔥 Сбор изображений
    images = []
    if product.image:
        images.append(product.image.url)

    additional_images = ProductImage.objects.filter(product=product).order_by('order', 'created_at')
    for img in additional_images:
        images.append(img.image.url)

    if not images and product.specifications and 'gallery' in product.specifications:
        images.extend(product.specifications['gallery'])

    is_in_cart = False
    is_favorited = False
    if request.user.is_authenticated:
        is_in_cart = CartItem.objects.filter(user=request.user, product=product).exists()
        is_favorited = Favorite.objects.filter(user=request.user, product=product).exists()

    return render(request, 'product/product_card.html', {
        'product': product,
        'is_in_cart': is_in_cart,
        'is_favorited': is_favorited,
        'reviews': reviews,
        'user_votes': votes_dict,
        'avg_rating': round(avg_rating, 1),
        'images': images,
        'rating_dist': rating_dist,
        'total_reviews': total_reviews,
    })


def add_review(request, slug):
    """Создание отзыва с полной валидацией"""
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug, is_active=True)
        rating = request.POST.get('rating', '').strip()
        comment = request.POST.get('comment', '').strip()

        # 🔥 ВАЛИДАЦИЯ ОЦЕНКИ
        if not rating:
            messages.error(request, 'Пожалуйста, поставьте оценку (выберите звёзды).')
            return redirect('catalog:product_detail', slug=slug)

        try:
            rating_int = int(rating)
            if not (1 <= rating_int <= 5):
                messages.error(request, 'Оценка должна быть от 1 до 5.')
                return redirect('catalog:product_detail', slug=slug)
        except (ValueError, TypeError):
            messages.error(request, 'Некорректная оценка.')
            return redirect('catalog:product_detail', slug=slug)

        # 🔥 ВАЛИДАЦИЯ КОММЕНТАРИЯ
        if not comment:
            messages.error(request, 'Заполните текст комментария.')
            return redirect('catalog:product_detail', slug=slug)

        # Авто-подстановка имени
        author_name = request.user.get_display_name() if request.user.is_authenticated else 'Гость'

        review = Review.objects.create(
            product=product,
            user=request.user if request.user.is_authenticated else None,
            author_name=author_name,
            rating=rating_int,
            pros=request.POST.get('pros', '').strip(),
            cons=request.POST.get('cons', '').strip(),
            comment=comment,
            has_issue=request.POST.get('has_issue') == 'on',
            issue_description=request.POST.get('issue_description', '').strip() if request.POST.get(
                'has_issue') == 'on' else '',
            is_verified_purchase=request.user.is_authenticated
        )

        # Файлы
        files = request.FILES.getlist('attachments')
        valid_count = 0
        for f in files:
            if f.content_type in ALLOWED_FILE_TYPES and f.size <= MAX_FILE_SIZE:
                f_type = 'image' if f.content_type.startswith('image/') else 'video'
                ReviewAttachment.objects.create(review=review, file=f, file_type=f_type)
                valid_count += 1

        if valid_count > 0:
            messages.success(request, f'Отзыв опубликован! Файлов: {valid_count}')
        else:
            messages.success(request, 'Отзыв опубликован!')

        return redirect('catalog:product_detail', slug=slug)

    return redirect('catalog:product_detail', slug=slug)


def search_view(request):
    """Умный поиск товаров с категориями"""
    query = request.GET.get('q', '').strip()
    products = Product.objects.filter(is_active=True).distinct()

    if query:
        # Умный поиск по словам
        words = query.split()
        q_objects = Q()
        for word in words:
            q_objects &= (
                    Q(title__icontains=word) |
                    Q(info__icontains=word) |
                    Q(description__icontains=word) |
                    Q(brand__icontains=word) |
                    Q(sku__icontains=word)
            )
        products = products.filter(q_objects)

    # 🔥 Получаем ВСЕ категории с количеством товаров
    categories_with_counts = products.values(
        'categories__slug',
        'categories__title',
        'categories__icon'
    ).annotate(
        count=Count('id')
    ).order_by('-count')

    # Основная категория (с наибольшим количеством)
    primary_category = None
    if categories_with_counts:
        top_cat = categories_with_counts[0]
        primary_category = {
            'slug': top_cat['categories__slug'],
            'title': top_cat['categories__title'],
            'icon': top_cat['categories__icon'],
            'count': top_cat['count'],
        }

    # Преобразуем queryset в список словарей для шаблона
    found_categories = [
        {
            'slug': cat['categories__slug'],
            'title': cat['categories__title'],
            'icon': cat['categories__icon'],
            'count': cat['count'],
        }
        for cat in categories_with_counts if cat['categories__slug']
    ]

    # Применяем фильтры
    target_slug = primary_category['slug'] if primary_category else None
    products = apply_filters(products, request, category_slug=target_slug)

    # Формируем конфиг фильтров
    filters = {}
    if target_slug:
        config = {**FILTERS_CONFIG.get('_common', {}), **FILTERS_CONFIG.get(target_slug, {})}
        base_products = products

        for key, spec in config.items():
            filter_data = {
                **spec,
                'value': request.GET.get(key),
                'selected_values': request.GET.getlist(key),
                'current_min': request.GET.get(f'{key}_min', ''),
                'current_max': request.GET.get(f'{key}_max', ''),
            }
            if spec['type'] == 'select':
                counts = {}
                for option in spec.get('options', []):
                    if key == 'brand':
                        counts[option] = base_products.filter(brand=option).count()
                    else:
                        counts[option] = base_products.filter(specifications__contains={key: option}).count()
                filter_data['counts'] = counts

                if key == 'brand':
                    brands = base_products.filter(brand__isnull=False).exclude(brand='').values('brand').annotate(
                        count=Count('id')).order_by('brand')
                    filter_data['options'] = [b['brand'] for b in brands]
                    filter_data['counts'] = {b['brand']: b['count'] for b in brands}

            filters[key] = filter_data

    # Аннотации
    products = products.annotate(
        reviews_count=Count('catalog_reviews'),
        avg_rating=Avg('catalog_reviews__rating'),
        is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
        is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
    ).prefetch_related('images')

    # Сортировка
    sort = request.GET.get('sort', 'popular')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'new':
        products = products.order_by('-created_at')
    elif sort == 'rating':
        products = products.order_by(Coalesce('avg_rating', 0).desc(), '-reviews_count', '-views')
    elif sort == 'reviews':
        products = products.order_by('-reviews_count', Coalesce('avg_rating', 0).desc(), '-views')
    else:
        products = products.order_by('-views')

    # Пагинация
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'catalog/search_results.html', {
        'query': query,
        'products': products_page,
        'primary_category': primary_category,
        'found_categories': found_categories,  # 🔥 Все найденные категории
        'filters': filters,
        'filter_params': filter_params.urlencode(),
    })


@login_required
def toggle_vote(request):
    """AJAX: Лайк/Дизлайк отзыва"""
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        vote_type = int(request.POST.get('vote'))
        review = get_object_or_404(Review, id=review_id)

        vote, created = ReviewVote.objects.update_or_create(
            review=review, user=request.user,
            defaults={'vote': vote_type}
        )
        if not created and vote.vote == vote_type:
            vote.delete()

        total_likes = review.votes.filter(vote=1).count()
        total_dislikes = review.votes.filter(vote=-1).count()
        return JsonResponse({'likes': total_likes, 'dislikes': total_dislikes})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def add_comment(request):
    """AJAX: Добавление комментария (JSON)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            review_id = data.get('review_id')
            raw_text = data.get('text', '')

            text = str(raw_text).strip()

            if not text or len(text) < 2:
                return JsonResponse({'error': 'Комментарий слишком короткий'}, status=400)

            review = get_object_or_404(Review, id=review_id)
            comment = ReviewComment.objects.create(
                review=review,
                user=request.user,
                text=text
            )

            return JsonResponse({
                'status': 'ok',
                'user': request.user.get_display_name(),
                'text': comment.text,
                'date': comment.created_at.strftime('%d.%m.%Y')
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)