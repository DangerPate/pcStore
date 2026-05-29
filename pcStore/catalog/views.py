# catalog/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Exists, OuterRef, Value, BooleanField
from catalog.models import Product, Category
from cart.models import CartItem, Favorite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def apply_filters(queryset, request):
    """Применяет фильтры из GET-параметров к queryset товаров"""

    # Цена
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min and price_min.isdigit():
        queryset = queryset.filter(price__gte=int(price_min))
    if price_max and price_max.isdigit():
        queryset = queryset.filter(price__lte=int(price_max))

    # Бренд
    brand = request.GET.get('brand')
    if brand:
        queryset = queryset.filter(brand=brand)

    # Наличие
    in_stock = request.GET.get('in_stock')
    if in_stock == '1':
        queryset = queryset.filter(in_stock__gt=0)

    # Сортировка
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        queryset = queryset.order_by('price')
    elif sort == 'price_desc':
        queryset = queryset.order_by('-price')

    return queryset


def category_view(request, category_slug):
    """Отображение товаров категории с фильтрами"""
    category = get_object_or_404(Category, slug=category_slug)

    # Базовая выборка
    products = Product.objects.filter(categories=category, is_active=True).distinct()

    # Применяем фильтры
    products = apply_filters(products, request)

    # Бренды для фильтра
    brands = Product.objects.filter(
        categories=category,
        is_active=True,
        brand__isnull=False
    ).exclude(brand='').values_list('brand', flat=True).distinct().order_by('brand')

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

    # 🔑 Формируем строку фильтров БЕЗ 'page' для пагинации
    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']
    filter_params_str = filter_params.urlencode()

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'products': products_page,
        'brands': brands,
        'filter_params': filter_params_str,  # 🔑 Передаём в шаблон!
    })


# catalog/views.py

def product_detail(request, slug):
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
    """Поиск товаров с фильтрами"""
    query = request.GET.get('q', '').strip()

    # Базовая выборка
    products = Product.objects.filter(is_active=True).distinct()

    # Поиск
    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(info__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__icontains=query)
        )

    # Применяем фильтры
    products = apply_filters(products, request)

    # Аннотации
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

    # 🔑 Формируем строку фильтров БЕЗ 'page' для пагинации
    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']
    filter_params_str = filter_params.urlencode()

    # 🔑 Получаем бренды для фильтра (все активные товары в поиске)
    brands = Product.objects.filter(
        is_active=True,
        brand__isnull=False
    ).exclude(brand='').values_list('brand', flat=True).distinct().order_by('brand')[:20]

    return render(request, 'catalog/search_results.html', {
        'query': query,
        'products': products_page,
        'total_count': paginator.count,
        'brands': brands,  # 🔑 Передаём бренды!
        'filter_params': filter_params_str,  # 🔑 Передаём filter_params!
    })