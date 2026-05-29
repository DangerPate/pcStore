from django.shortcuts import render
from catalog.models import Product, Category
from django.db.models import Exists, OuterRef, Value, BooleanField, Q, F
from cart.models import CartItem, Favorite
from .models import Banner


# main/views.py

# main/views.py

def index(request):
    """Главная страница с баннерами и каруселями"""

    # === БАННЕРЫ С ТОВАРАМИ ===
    banners_with_products = []
    active_banners = Banner.objects.filter(
        is_active=True
    ).select_related('link_category', 'link_product').prefetch_related('products')

    for banner in active_banners:
        if banner.is_current:
            discounted_products = banner.get_discounted_products(count=3)

            if request.user.is_authenticated:
                discounted_products = discounted_products.annotate(
                    is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
                    is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
                )
            else:
                discounted_products = discounted_products.annotate(
                    is_in_cart=Value(False, output_field=BooleanField()),
                    is_favorited=Value(False, output_field=BooleanField())
                )

            banners_with_products.append({
                'banner': banner,
                'products': list(discounted_products),
            })

    # === 🔥 ТОВАРЫ СО СКИДКОЙ ===
    discounted_products_all = Product.objects.filter(
        is_active=True,
        old_price__isnull=False
    ).exclude(
        old_price__lte=F('price')
    ).order_by('-created_at')[:15]

    if request.user.is_authenticated:
        discounted_products_all = discounted_products_all.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        discounted_products_all = discounted_products_all.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    # === ОБЫЧНЫЕ ТОВАРЫ ===
    products = Product.objects.filter(is_active=True)[:15]

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
    # main/views.py — внутри функции index(), после discounted_products_all

    # === 🔥 ХИТЫ ПРОДАЖ ===
    hit_products = Product.objects.filter(
        is_active=True
    ).order_by('-created_at')[:15]

    new_products = Product.objects.filter(
        is_active=True
    ).order_by('-created_at')[:15]


    if request.user.is_authenticated:
        hit_products = hit_products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        hit_products = hit_products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    return render(request, 'main/index.html', {
        'banners_with_products': banners_with_products,
        'discounted_products': discounted_products_all,
        'hit_products': hit_products,
        'new_products': new_products,
        'products': products,
    })
def about(request):
    return render(request, 'main/info/about.html')

def delivery(request):
    return render(request, 'main/info/delivery.html', {'title': 'Доставка и оплата'})

def warranty(request):
    return render(request, 'main/info/warranty.html', {'title': 'Гарантия'})

def returns(request):
    return render(request, 'main/info/returns.html', {'title': 'Возврат товара'})

def privacy(request):
    return render(request, 'main/info/privacy.html', {'title': 'Политика конфиденциальности'})

def terms(request):
    return render(request, 'main/info/terms.html', {'title': 'Пользовательское соглашение'})

def public_offer(request):
    return render(request, 'main/info/public_offer.html', {'title': 'Публичная оферта'})

def faq(request):
    return render(request, 'main/info/faq.html', {'title': 'Частые вопросы'})

def vacancies(request):
    return render(request, 'main/info/vacancies.html')

def partners(request):
    return render(request, 'main/info/partners.html')
