from django.shortcuts import render
from catalog.models import Product, Category, Promotion
from django.db.models import Exists, OuterRef, Value, BooleanField, Q, F, Count, Avg
from cart.models import CartItem, Favorite
from .models import Banner


def index(request):
    """Главная страница с баннерами и каруселями"""

    base_products = Product.objects.filter(is_active=True)

    # 🔥 ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ для безопасной аннотации
    # Если пользователь вошел - проверяем его корзину/избранное.
    # Если нет - просто ставим False, чтобы не крашить БД объектом AnonymousUser.
    def annotate_products(qs):
        if request.user.is_authenticated:
            return qs.annotate(
                reviews_count=Count('catalog_reviews'),
                avg_rating=Avg('catalog_reviews__rating'),
                is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
                is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
            ).prefetch_related('images')
        else:
            return qs.annotate(
                reviews_count=Count('catalog_reviews'),
                avg_rating=Avg('catalog_reviews__rating'),
                is_in_cart=Value(False, output_field=BooleanField()),
                is_favorited=Value(False, output_field=BooleanField())
            ).prefetch_related('images')

    # === 1. БАННЕРЫ С ТОВАРАМИ ===
    banners_with_products = []
    active_banners = Banner.objects.filter(
        is_active=True
    ).select_related('link_category', 'link_product').prefetch_related('products')

    for banner in active_banners:
        if getattr(banner, 'is_current', True):  # Безопасная проверка, если поля is_current нет
            products_qs = banner.products.filter(is_active=True)
            products_qs = annotate_products(products_qs)  # 🔥 Безопасная аннотация

            banners_with_products.append({
                'banner': banner,
                'products': list(products_qs[:3]),
            })

    # === 2. ТОВАРЫ СО СКИДКОЙ ===
    discounted_products_all = annotate_products(
        base_products.filter(
            old_price__isnull=False
        ).exclude(old_price__lte=F('price')).order_by('-created_at')[:15]
    )

    # === 3. ПОПУЛЯРНОЕ ===
    popular_products = annotate_products(
        base_products.filter(views__gt=0).order_by('-views')[:15]
    )

    # === 4. НОВИНКИ ===
    new_products = annotate_products(
        base_products.order_by('-created_at')[:15]
    )

    # === 5. АКЦИИ (Promotions) ===
    promotions = Promotion.objects.filter(
        is_active=True,
        products__isnull=False
    ).distinct().order_by('order', '-created_at')[:5]

    # === 6. СЧЕТЧИКИ ДЛЯ НАВБАРА ===
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_count = Favorite.objects.filter(user=request.user).count()
    else:
        cart_count = 0
        fav_count = 0

    return render(request, 'main/index.html', {
        'banners_with_products': banners_with_products,
        'discounted_products': discounted_products_all,
        'popular_products': popular_products,
        'new_products': new_products,
        'promotions': promotions,
        'cart_count': cart_count,  # 🔥 Передаем для навбара
        'fav_count': fav_count,  # 🔥 Передаем для навбара
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