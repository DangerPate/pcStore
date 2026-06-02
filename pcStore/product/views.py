
from django.shortcuts import render, get_object_or_404
from cart.models import CartItem, Favorite
from catalog.models import Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    is_in_cart = False
    is_favorited = False

    if request.user.is_authenticated:

        cart_item = CartItem.objects.filter(
            cart__user=request.user,
            product=product
        ).first()

        fav_item = Favorite.objects.filter(
            user=request.user,
            product=product
        ).first()

        is_in_cart = cart_item is not None
        is_favorited = fav_item is not None

        print(f"\n📦 DEBUG product_detail:")
        print(f"   User: {request.user.email} (ID: {request.user.id})")
        print(f"   Product: {product.title} (slug: {slug})")
        print(f"   Cart exists: {is_in_cart}")
        if cart_item:
            print(f"   → CartItem: id={cart_item.id}, qty={cart_item.quantity}")
        print(f"   Favorite exists: {is_favorited}")
        if fav_item:
            print(f"   → Favorite: id={fav_item.id}")

        from cart.models import Cart
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items_count = cart.items.count()
            print(f"   Cart ID: {cart.id}, items count: {cart_items_count}")
            if cart_items_count > 0:
                print(f"   → Items in cart:")
                for item in cart.items.all():
                    print(f"      - {item.product.title} (qty: {item.quantity})")
        else:
            print(f"   ⚠️ Cart not found for user {request.user.email}")
        print()

    return render(request, 'product/product_card.html', {
        'product': product,
        'is_in_cart': is_in_cart,
        'is_favorited': is_favorited,
    })