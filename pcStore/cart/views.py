# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Cart, CartItem, Favorite
from catalog.models import Product
from django.db.models import Exists, OuterRef, Sum


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('product').prefetch_related('product__categories')

    # Считаем ВСЕ товары (для отображения)
    total_count = items.count()
    total_price = items.aggregate(total=Sum('product__price'))['total'] or 0

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'items': items,
        'total_count': total_count,
        'total_price': total_price
    })


@login_required
def bulk_cart_action(request):
    """Обработка массовых действий: удалить выбранные"""
    if request.method == 'POST':
        action = request.POST.get('action')
        item_ids = request.POST.getlist('item_ids')

        cart, _ = Cart.objects.get_or_create(user=request.user)

        if action == 'delete_selected' and item_ids:
            deleted = cart.items.filter(id__in=item_ids).delete()[0]
            messages.success(request, f'Удалено {deleted} товар{{ "а" if deleted in [2,3,4] else "ов" }}')

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Пересчитываем итоги
            items = cart.items.select_related('product')
            return JsonResponse({
                'status': 'ok',
                'total_count': items.count(),
                'total_price': items.aggregate(total=Sum('product__price'))['total'] or 0
            })

        return redirect('cart:cart')


@login_required
def checkout_selected(request):
    """Оформление заказа ТОЛЬКО выбранных товаров"""
    if request.method == 'POST':
        item_ids = request.POST.getlist('item_ids')
        if not item_ids:
            messages.warning(request, 'Выберите товары для оформления')
            return redirect('cart:cart')

        cart = get_object_or_404(Cart, user=request.user)
        selected_items = cart.items.filter(id__in=item_ids).select_related('product')

        if not selected_items.exists():
            messages.warning(request, 'Выбранные товары не найдены')
            return redirect('cart:cart')

        # 🔑 Здесь будет логика создания заказа
        # order = Order.objects.create(user=request.user, total_price=..., ...)
        # for item in selected_items:
        #     OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        #     item.delete()  # Удаляем из корзины после заказа

        # Заглушка для теста:
        total = sum(item.product.price * item.quantity for item in selected_items)
        messages.success(request, f'✅ Заказ оформлен! Сумма: {total} ₽ (товаров: {selected_items.count()})')

        # Опционально: удалить оформленные товары из корзины
        # selected_items.delete()

        return redirect('cart:cart')

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
    favorites = Favorite.objects.filter(user=request.user).select_related('product').prefetch_related(
        'product__categories')

    favorites = favorites.annotate(
        is_in_cart=Exists(CartItem.objects.filter(cart__user=request.user, product_id=OuterRef('product_id')))
    )

    # 🔑 Считаем итоги
    total_count = favorites.count()
    total_price = favorites.aggregate(total=Sum('product__price'))['total'] or 0

    return render(request, 'cart/favorites.html', {
        'favorites': favorites,
        'total_count': total_count,
        'total_price': total_price
    })


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