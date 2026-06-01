from django.shortcuts import render
from catalog.models import Product, Category
from django.db.models import Exists, OuterRef, Value, BooleanField, Q, F, Count, Avg
from cart.models import CartItem, Favorite
from .models import Banner


def index(request):
    """Главная страница с баннерами и каруселями"""

    base_products = Product.objects.filter(is_active=True)

    # === 1. БАННЕРЫ С ТОВАРАМИ ===
    banners_with_products = []
    active_banners = Banner.objects.filter(
        is_active=True
    ).select_related('link_category', 'link_product').prefetch_related('products')

    for banner in active_banners:
        if banner.is_current:
            products_qs = banner.products.filter(is_active=True)

            # 🔥 Аннотации с УНИКАЛЬНЫМ именем reviews_count
            products_qs = products_qs.annotate(
                reviews_count=Count('catalog_reviews'),  # 🔥 Было review_count
                avg_rating=Avg('catalog_reviews__rating'),
                is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
                is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
            ).prefetch_related('images')

            banners_with_products.append({
                'banner': banner,
                'products': list(products_qs[:3]),
            })

    # === 2. ТОВАРЫ СО СКИДКОЙ ===
    discounted_products_all = base_products.filter(
        old_price__isnull=False
    ).exclude(old_price__lte=F('price')
              ).annotate(
        reviews_count=Count('catalog_reviews'),  # 🔥 Было review_count
        avg_rating=Avg('catalog_reviews__rating'),
        is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
        is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
    ).prefetch_related('images').order_by('-created_at')[:15]

    # === 3. ПОПУЛЯРНОЕ ===
    popular_products = base_products.filter(
        views__gt=0
    ).annotate(
        reviews_count=Count('catalog_reviews'),  # 🔥 Было review_count
        avg_rating=Avg('catalog_reviews__rating'),
        is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
        is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
    ).prefetch_related('images').order_by('-views')[:15]

    # === 4. НОВИНКИ ===
    new_products = base_products.annotate(
        reviews_count=Count('catalog_reviews'),  # 🔥 Было review_count
        avg_rating=Avg('catalog_reviews__rating'),
        is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
        is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
    ).prefetch_related('images').order_by('-created_at')[:15]

    return render(request, 'main/index.html', {
        'banners_with_products': banners_with_products,
        'discounted_products': discounted_products_all,
        'popular_products': popular_products,
        'new_products': new_products,
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