# cart/context_processors.py
from cart.models import CartItem, Favorite


def cart_fav_counts(request):
    """Добавляет количество товаров в корзине и избранном в контекст"""
    ctx = {'cart_count': 0, 'fav_count': 0}

    if request.user.is_authenticated:
        # 🔑 Считаем напрямую через CartItem, привязанный к user
        ctx['cart_count'] = CartItem.objects.filter(user=request.user).count()

        # Считаем избранное
        ctx['fav_count'] = Favorite.objects.filter(user=request.user).count()

    return ctx