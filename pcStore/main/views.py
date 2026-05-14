from django.shortcuts import render
from catalog.models import Product, Category
from django.db.models import Exists, OuterRef, Value, BooleanField
from cart.models import CartItem, Favorite


def index(request):
    products = Product.objects.filter(is_active=True)[:15]  # Ваши 12 товаров

    if request.user.is_authenticated:
        products = products.annotate(
            is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product=OuterRef('pk'))),
            is_favorited=Exists(Favorite.objects.filter(user=request.user, product=OuterRef('pk')))
        )
    else:
        # 🔑 FIX: Используем Value() вместо простого False
        products = products.annotate(
            is_in_cart=Value(False, output_field=BooleanField()),
            is_favorited=Value(False, output_field=BooleanField())
        )

    return render(request, 'main/index.html', {'products': products})

def about(request):
    return render(request, 'main/about.html')