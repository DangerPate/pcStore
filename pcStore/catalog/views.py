# catalog/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Exists, OuterRef, Value, BooleanField
from catalog.models import Product, Category
from cart.models import CartItem, Favorite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters_config import FILTERS_CONFIG


def apply_filters(queryset, request, category_slug=None):
    """
    Объединяет общие фильтры (цена, бренд, наличие, сортировка)
    и динамические JSON-фильтры для конкретной категории.
    """
    # === 1. ОБЩИЕ ФИЛЬТРЫ (работают везде: категории + поиск) ===
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_min.isdigit():
        queryset = queryset.filter(price__gte=int(price_min))
    if price_max and price_max.isdigit():
        queryset = queryset.filter(price__lte=int(price_max))

    brand = request.GET.get('brand')
    if brand:
        queryset = queryset.filter(brand__icontains=brand)

    if request.GET.get('in_stock') == '1':
        queryset = queryset.filter(in_stock__gt=0)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        queryset = queryset.order_by('price')
    elif sort == 'price_desc':
        queryset = queryset.order_by('-price')
    elif not sort:
        queryset = queryset.order_by('-created_at')  # Дефолтная сортировка

    # === 2. ДИНАМИЧЕСКИЕ ФИЛЬТРЫ (только для категорий из CONFIG) ===
    if category_slug and category_slug in FILTERS_CONFIG:
        specs_config = FILTERS_CONFIG[category_slug]

        for key, spec in specs_config.items():

            #  Выпадающие списки (select)
            if spec['type'] == 'select':
                value = request.GET.get(key)
                if value:
                    queryset = queryset.filter(specifications__contains={key: value})

            # 🔹 Диапазоны (range) для частот, TDP и т.д.
            elif spec['type'] == 'range':
                min_val = request.GET.get(f'{key}_min')
                max_val = request.GET.get(f'{key}_max')

                if min_val or max_val:
                    try:
                        # Преобразуем в float для корректного сравнения
                        min_f = float(min_val) if min_val else None
                        max_f = float(max_val) if max_val else None

                        # Используем нативные фильтры Django для JSONField (работает в PostgreSQL)
                        if min_f is not None:
                            queryset = queryset.filter(**{f'specifications__{key}__gte': min_f})
                        if max_f is not None:
                            queryset = queryset.filter(**{f'specifications__{key}__lte': max_f})
                    except ValueError:
                        pass  # Игнорируем некорректные числа, чтобы не ломать запрос

    return queryset


def category_view(request, category_slug):
    """Отображение товаров категории с динамическими фильтрами"""
    category = get_object_or_404(Category, slug=category_slug)

    # Базовая выборка
    products = Product.objects.filter(categories=category, is_active=True).distinct()

    # Применяем фильтры (передаём slug для включения динамических правил)
    products = apply_filters(products, request, category_slug)

    # 🔥 ФОРМИРУЕМ КОНФИГУРАЦИЮ ФИЛЬТРОВ ДЛЯ ШАБЛОНА
    config = {**FILTERS_CONFIG.get('_common', {}), **FILTERS_CONFIG.get(category_slug, {})}

    if 'brand' in config:
        config['brand']['options'] = list(
            Product.objects.filter(categories=category, is_active=True, brand__isnull=False)
            .exclude(brand='').values_list('brand', flat=True).distinct().order_by('brand')
        )

    # 🔑 ДОБАВЛЕНО: сохраняем текущие значения диапазонов
    filters = {}
    for key, spec in config.items():
        filters[key] = {
            **spec,
            'value': request.GET.get(key),
            'current_min': request.GET.get(f'{key}_min', ''),
            'current_max': request.GET.get(f'{key}_max', ''),
        }

    # Аннотации для кнопок корзины/избранного
    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        products = products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    # Пагинация
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    # Параметры для пагинации
    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'products': products_page,
        'filters': filters,  # 🔑 ЗАМЕНЯЕТ 'brands'
        'filter_params': filter_params.urlencode(),
    })


def product_detail(request, slug):
    """Детальная страница товара"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    product.increment_views()

    is_in_cart = False
    is_favorited = False

    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=request.user, product=product).first()
        fav_item = Favorite.objects.filter(user=request.user, product=product).first()
        is_in_cart = cart_item is not None
        is_favorited = fav_item is not None

    return render(request, 'product/product_card.html', {
        'product': product,
        'is_in_cart': is_in_cart,
        'is_favorited': is_favorited,
    })


def search_view(request):
    """Поиск товаров с общими фильтрами"""
    query = request.GET.get('q', '').strip()
    products = Product.objects.filter(is_active=True).distinct()

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(info__icontains=query) |
            Q(description__icontains=query) | Q(brand__icontains=query)
        )

    # Поиск использует только общие фильтры (category_slug=None)
    products = apply_filters(products, request)

    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        products = products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

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
        'total_count': paginator.count,
        'filter_params': filter_params.urlencode(),
        # 🔑 Для поиска оставляем упрощённый рендер брендов, если нужно
    })