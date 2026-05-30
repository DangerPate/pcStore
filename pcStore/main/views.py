from django.shortcuts import render
from catalog.models import Product, Category
from django.db.models import Exists, OuterRef, Value, BooleanField, Q, F
from cart.models import CartItem, Favorite
from .models import Banner


def index(request):
    """Главная страница с баннерами и каруселями"""

    # === 1. БАННЕРЫ С ТОВАРАМИ ===
    banners_with_products = []
    active_banners = Banner.objects.filter(
        is_active=True
    ).select_related('link_category', 'link_product').prefetch_related('products')

    for banner in active_banners:
        if banner.is_current:
            # 🔑 ИСПРАВЛЕНИЕ: работаем с QuerySet, а не со списком
            # get_discounted_products возвращал list, у которого нет .annotate()
            products_qs = banner.products.filter(is_active=True)

            if request.user.is_authenticated:
                products_qs = products_qs.annotate(
                    is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
                    is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
                )
            else:
                products_qs = products_qs.annotate(
                    is_in_cart=Value(False, output_field=BooleanField()),
                    is_favorited=Value(False, output_field=BooleanField())
                )

            # 🔑 Преобразуем в список ТОЛЬКО после аннотаций и ограничения выборки
            banners_with_products.append({
                'banner': banner,
                'products': list(products_qs[:3]),
            })

    # === 2. ТОВАРЫ СО СКИДКОЙ ===
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

    # === 3. ПОПУЛЯРНОЕ (только товары с максимальным количеством просмотров) ===
    popular_products = Product.objects.filter(
        is_active=True,
        views__gt=0  # 🔑 Исключаем товары с 0 просмотров
    ).order_by('-views')[:15]  # 🔑 Сортировка строго по убыванию просмотров

    if request.user.is_authenticated:
        popular_products = popular_products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        popular_products = popular_products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    # === 4. НОВИНКИ (автоматически по дате создания) ===
    new_products = Product.objects.filter(is_active=True).order_by('-created_at')[:15]

    if request.user.is_authenticated:
        new_products = new_products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        new_products = new_products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    return render(request, 'main/index.html', {
        'banners_with_products': banners_with_products,
        'discounted_products': discounted_products_all,
        'popular_products': popular_products,  # 🔑 Новое имя
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