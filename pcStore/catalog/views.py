from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db.models import Exists, OuterRef, Value, BooleanField
from catalog.models import Product, Category
from cart.models import Cart, CartItem, Favorite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Замените существующий category_view на:
# catalog/views.py
def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(categories=category, is_active=True).distinct()

    # Применяем фильтры
    products = apply_filters(products, request)

    # Аннотации (Корзина/Избранное)
    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product=OuterRef('pk'))),
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

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'products': products_page,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    is_in_cart = False
    is_favorited = False

    if request.user.is_authenticated:
        # 🔍 Проверяем БД
        cart_item = CartItem.objects.filter(
            cart__user=request.user,
            product=product
        ).first()

        fav_item = Favorite.objects.filter(
            user=request.user,
            product=product
        ).first()

        is_in_cart = cart_item is not None
        is_favorited = fav_item is not None

        # 🔥 ОТЛАДКА
        print(f"\n📦 DEBUG product_detail:")
        print(f"   User: {request.user.email} (ID: {request.user.id})")
        print(f"   Product: {product.title}")
        print(f"   In cart: {is_in_cart}, Favorited: {is_favorited}")
        print()

    return render(request, 'product/product_card.html', {
        'product': product,
        'is_in_cart': is_in_cart,
        'is_favorited': is_favorited,
    })


# catalog/views.py
def search_view(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.filter(is_active=True).distinct()

    if query:
        products = products.filter(Q(title__icontains=query) | Q(info__icontains=query))

    # Применяем фильтры
    products = apply_filters(products, request)

    # ... (аннотации такие же как выше) ...
    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product=OuterRef('pk'))),
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

    return render(request, 'catalog/search_results.html', {
        'query': query,
        'products': products_page,
        'total_count': paginator.count,
    })


def apply_filters(queryset, request):
    """Функция, которая применяет все фильтры к списку товаров"""

    # 1. Цена
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if price_min and price_min.isdigit():
        queryset = queryset.filter(price__gte=int(price_min))
    if price_max and price_max.isdigit():
        queryset = queryset.filter(price__lte=int(price_max))

    # 2. Бренд (если поле brand есть в модели Product)
    brand = request.GET.get('brand')
    if brand:
        queryset = queryset.filter(brand=brand)

    # 3. Наличие
    in_stock = request.GET.get('in_stock')
    if in_stock == '1':
        queryset = queryset.filter(in_stock__gt=0)

    # 4. СПЕЦИФИЧЕСКИЕ ХАРАКТЕРИСТИКИ (Пример)
    # Если у тебя есть поля вроде ram_size, socket_type и т.д.
    ram = request.GET.get('ram')
    if ram:
        queryset = queryset.filter(ram=ram)

    socket = request.GET.get('socket')
    if socket:
        queryset = queryset.filter(socket=socket)

    # 5. Сортировка
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        queryset = queryset.order_by('price')
    elif sort == 'price_desc':
        queryset = queryset.order_by('-price')
    # По умолчанию сортировка по id (новые сверху) или как настроено в Meta

    return queryset

def build_filter_params(request, exclude_page=True):
    """Строит строку параметров фильтров для пагинации"""
    params = request.GET.copy()
    if exclude_page and 'page' in params:
        del params['page']
    return params.urlencode() if params else ''

