from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.db.models import Exists, OuterRef
from cart.models import CartItem, Favorite
def mini_product_card(request):
    products = Product.objects.all()
    return render(request, 'product/mini_product_card.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    if request.user.is_authenticated:
        # 🔑 Явно проверяем и добавляем атрибуты к объекту
        product.is_in_cart = CartItem.objects.filter(
            cart__user=request.user,
            product=product
        ).exists()
        product.is_favorited = Favorite.objects.filter(
            user=request.user,
            product=product
        ).exists()
    else:
        product.is_in_cart = False
        product.is_favorited = False

    return render(request, 'product/product_card.html', {'product': product})