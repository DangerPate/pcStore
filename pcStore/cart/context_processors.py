from .models import Cart, Favorite

def cart_fav_counts(request):
    ctx = {'cart_count': 0, 'fav_count': 0}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        ctx['cart_count'] = cart.get_total_quantity() if cart else 0
        ctx['fav_count'] = Favorite.objects.filter(user=request.user).count()
    return ctx