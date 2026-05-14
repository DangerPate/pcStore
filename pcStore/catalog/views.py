from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from catalog.models import Product
from django.db.models import Q
from cart.models import CartItem, Favorite
from django.db.models import Exists, OuterRef


# Замените существующий category_view на:
# catalog/views.py
def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(categories=category, is_active=True)

    if request.user.is_authenticated:
        from django.db.models import Exists, OuterRef
        from cart.models import CartItem, Favorite

        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        ).prefetch_related('categories')  # 🔑 Один запрос на все категории
    else:
        from django.db.models import Value, BooleanField
        products = products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        ).prefetch_related('categories')

    return render(request, 'catalog/catalog.html', {'category': category, 'products': products})


def product_detail(request, slug):
    """Рендерит ваш готовый шаблон product_card.html"""
    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'product/product_card.html', {'product': product})


def search_view(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return render(request, 'catalog/search_results.html', {
            'query': '', 'products': Product.objects.none(),
            'categories_count': {}, 'total_count': 0
        })

    products = Product.objects.filter(
        Q(title__icontains=query) | Q(info__icontains=query) |
        Q(brand__icontains=query) | Q(categories__title__icontains=query),
        is_active=True
    ).distinct()

    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        products = products.annotate(is_in_cart=False, is_favorited=False)

    categories_count = {}
    for category in Category.objects.all():
        count = products.filter(categories=category).count()
        if count > 0: categories_count[category] = count

    return render(request, 'catalog/search_results.html', {
        'query': query, 'products': products,
        'categories_count': categories_count, 'total_count': products.count()
    })