# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Cart, CartItem, Favorite
from catalog.models import Product
from django.db.models import Prefetch

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def add_to_cart(request, product_slug):
    print(f"\n🛒 DEBUG add_to_cart:")
    print(f"   User: {request.user.email} (ID: {request.user.id})")
    print(f"   Product slug: {product_slug}")

    product = get_object_or_404(Product, slug=product_slug, is_active=True)
    print(f"   Product found: {product.title} (ID: {product.id})")

    cart, created = Cart.objects.get_or_create(user=request.user)
    print(f"   Cart: id={cart.id}, created={created}")

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
        print(f"   CartItem exists, quantity increased to {item.quantity}")
    else:
        print(f"   CartItem created with quantity 1")

    print(f"   Total items in cart: {cart.get_total_quantity()}\n")

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'total': cart.get_total_quantity()})

    messages.success(request, f'"{product.title}" добавлен в корзину')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        qty = int(request.POST.get('quantity', 1))
        if qty > 0:
            item.quantity = qty
            item.save()
        else:
            item.delete()
        return redirect('cart:cart')


@login_required
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        item.delete()
        return redirect('cart:cart')


@login_required
def favorites_view(request):
    # 🔑 prefetch_related загружает все товары одним запросом
    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related('product').prefetch_related('product__categories')

    return render(request, 'cart/favorites.html', {'favorites': favorites})


@login_required
def toggle_favorite(request, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug, is_active=True)
        fav, created = Favorite.objects.get_or_create(user=request.user, product=product)
        if not created:
            fav.delete()
            is_fav = False
        else:
            is_fav = True

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok', 'is_favorited': is_fav})
        return redirect(request.META.get('HTTP_REFERER', 'home'))