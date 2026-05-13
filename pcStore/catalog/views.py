from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from catalog.models import Product
from django.db.models import Q

def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()
    if request.GET.get('price_min'):
        products = products.filter(price__gte=request.GET['price_min'])
    if request.GET.get('price_max'):
        products = products.filter(price__lte=request.GET['price_max'])
    if request.GET.get('in_stock') == '1':
        products = products.filter(in_stock__gt=0)
    return render(request, 'catalog/catalog.html', {'category': category, 'products': products})


def product_detail(request, slug):
    """Рендерит ваш готовый шаблон product_card.html"""
    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'product/product_card.html', {'product': product})


def search_view(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return render(request, 'catalog/search_results.html', {
            'query': '',
            'products': Product.objects.none(),
            'categories_count': {},
        })

    # Ищем товары по всем категориям
    products = Product.objects.filter(
        Q(title__icontains=query) |
        Q(info__icontains=query) |
        Q(brand__icontains=query) |
        Q(categories__title__icontains=query),
        is_active=True
    ).distinct()

    # Считаем количество товаров по категориям
    categories_count = {}
    for category in Category.objects.all():
        count = products.filter(categories=category).count()
        if count > 0:
            categories_count[category] = count

    return render(request, 'catalog/search_results.html', {
        'query': query,
        'products': products,
        'categories_count': categories_count,
        'total_count': products.count(),
    })