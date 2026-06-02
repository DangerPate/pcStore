# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Exists, OuterRef, Sum, F
from .models import CartItem, Favorite, Order, OrderItem
from .forms import CheckoutForm
from catalog.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def checkout_selected(request):
    """Оформление заказа"""
    # Если корзина пуста, редиректим обратно
    if not CartItem.objects.filter(user=request.user).exists():
        return redirect('cart:cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Получаем ID выбранных товаров (их добавляет JS из cart.html)
            item_ids = request.POST.getlist('item_ids')

            cart_items = CartItem.objects.filter(user=request.user)
            if item_ids:
                cart_items = cart_items.filter(id__in=item_ids)

            if not cart_items.exists():
                messages.error(request, 'Выберите товары для оформления.')
                return redirect('cart:cart')

            # Считаем общую сумму
            total_price = sum(item.get_total_price() for item in cart_items)

            # Создаем заказ
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total_price = total_price
            order.save()

            # Создаем элементы заказа и удаляем их из корзины
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )

            # Очищаем корзину от оформленных товаров
            cart_items.delete()

            messages.success(request, f'Заказ #{order.id} успешно оформлен! Мы свяжемся с вами в ближайшее время.')
            return redirect('home')  # Или на специальную страницу успеха
    else:
        # Предзаполняем форму, если пользователь авторизован
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['first_name'] = request.user.get_full_name() or request.user.username
            initial_data['email'] = request.user.email
        form = CheckoutForm(initial=initial_data)

    # Получаем товары для отображения в чеке на странице оформления
    item_ids = request.POST.getlist('item_ids')  # Если пришли с POST
    if not item_ids:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = CartItem.objects.filter(user=request.user, id__in=item_ids)

    return render(request, 'cart/checkout.html', {
        'form': form,
        'cart_items': cart_items,
    })


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


@login_required
def orders_list(request):
    """Список заказов пользователя"""
    # Получаем все заказы текущего пользователя
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Пагинация
    paginator = Paginator(orders, 10)  # По 10 заказов на странице

    # 🔥 Добавляем значение по умолчанию '1', если параметра page нет в URL
    page_number = request.GET.get('page', 1)

    try:
        orders_page = paginator.page(page_number)
    except PageNotAnInteger:
        # Если передано не число, показываем первую страницу
        orders_page = paginator.page(1)
    except EmptyPage:
        # Если страница вне диапазона (например, 9999), показываем последнюю
        orders_page = paginator.page(paginator.num_pages)

    return render(request, 'cart/orders.html', {
        'orders': orders_page,
    })


@login_required
def order_detail(request, order_id):
    """Детальная страница конкретного заказа"""
    # Получаем заказ и проверяем, что он принадлежит текущему пользователю
    order = get_object_or_404(Order, id=order_id, user=request.user)

    return render(request, 'cart/order_detail.html', {
        'order': order,
    })