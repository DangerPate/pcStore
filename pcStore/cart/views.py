# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Exists, OuterRef, Sum, F
from .models import CartItem, Favorite
from catalog.models import Product


@login_required
def cart_view(request):
    """Отображение корзины текущего пользователя"""
    # 🔑 Прямой запрос: только товары ЭТОГО пользователя
    items = CartItem.objects.filter(
        user=request.user
    ).select_related('product').prefetch_related('product__categories')

    total_count = items.count()
    total_price = items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0

    return render(request, 'cart/cart.html', {
        'items': items,
        'total_count': total_count,
        'total_price': total_price,
    })


@login_required
def bulk_cart_action(request):
    """Массовые действия с корзиной: удалить выбранные"""
    if request.method == 'POST':
        action = request.POST.get('action')
        item_ids = request.POST.getlist('item_ids')

        if action == 'delete_selected' and item_ids:
            # 🔑 Безопасное удаление: только свои товары
            deleted, _ = CartItem.objects.filter(
                user=request.user,
                id__in=item_ids
            ).delete()
            messages.success(request, f'Удалено {deleted} товар{"а" if deleted in [2, 3, 4] else "ов"}')

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            items = CartItem.objects.filter(user=request.user).select_related('product')
            total = items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0
            return JsonResponse({
                'status': 'ok',
                'total_count': items.count(),
                'total_price': total,
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

        # 🔑 Только свои товары
        selected_items = CartItem.objects.filter(
            user=request.user,
            id__in=item_ids
        ).select_related('product')

        if not selected_items.exists():
            messages.warning(request, 'Выбранные товары не найдены')
            return redirect('cart:cart')

        # 🔑 Заглушка для теста:
        total = sum(item.product.price * item.quantity for item in selected_items)
        messages.success(request, f'✅ Заказ оформлен! Сумма: {total} ₽ (товаров: {selected_items.count()})')

        # Раскомментируй, когда будешь готов удалять товары после заказа:
        # selected_items.delete()

        return redirect('cart:cart')


@login_required
def add_to_cart(request, product_slug):
    """Добавление товара в корзину"""
    product = get_object_or_404(Product, slug=product_slug, is_active=True)

    # 🔑 Прямая привязка к пользователю: get_or_create гарантирует уникальность (user, product)
    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        # Если товар уже был — увеличиваем количество
        item.quantity = F('quantity') + 1
        item.save()
        # Перезагружаем объект, чтобы получить актуальное значение quantity
        item.refresh_from_db()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        total = CartItem.objects.filter(user=request.user).count()
        return JsonResponse({'status': 'ok', 'total': total})

    messages.success(request, f'"{product.title}" добавлен в корзину')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def update_cart(request, item_id):
    """Обновление количества товара в корзине"""
    if request.method == 'POST':
        # 🔑 Безопасный запрос: только свой товар
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        qty = int(request.POST.get('quantity', 1))

        if qty > 0:
            item.quantity = qty
            item.save()
        else:
            item.delete()

        return redirect('cart:cart')


@login_required
def remove_from_cart(request, item_id):
    """Удаление товара из корзины"""
    if request.method == 'POST':
        # 🔑 Безопасный запрос: только свой товар
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        item.delete()
        return redirect('cart:cart')


@login_required
def favorites_view(request):
    """Отображение избранного текущего пользователя"""
    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related('product').prefetch_related('product__categories')

    # 🔑 Проверяем, есть ли товар в корзине ЭТОГО пользователя
    favorites = favorites.annotate(
        is_in_cart=Exists(
            CartItem.objects.filter(
                user=request.user,  # 🔑 Только корзина текущего пользователя
                product_id=OuterRef('product_id')
            )
        )
    )

    total_count = favorites.count()
    total_price = favorites.aggregate(total=Sum('product__price'))['total'] or 0

    return render(request, 'cart/favorites.html', {
        'favorites': favorites,
        'total_count': total_count,
        'total_price': total_price,
    })


@login_required
def toggle_favorite(request, product_slug):
    """Добавление/удаление товара из избранного"""
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug, is_active=True)

        # 🔑 Прямая привязка к пользователю
        fav, created = Favorite.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            fav.delete()
            is_fav = False
        else:
            is_fav = True

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok', 'is_favorited': is_fav})

        return redirect(request.META.get('HTTP_REFERER', 'home'))