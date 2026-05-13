from django.shortcuts import render, get_object_or_404
from .models import Category
from catalog.models import Product

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
