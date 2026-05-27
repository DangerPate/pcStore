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
    return render(request, 'main/info/about.html')

def delivery(request):
    return render(request, 'main/info/delivery.html', {'title': 'Доставка и оплата'})

def warranty(request):
    return render(request, 'main/info/warranty.html', {'title': 'Гарантия'})

def returns(request):
    return render(request, 'main/info/returns.html', {'title': 'Возврат товара'})

def credit(request):
    return render(request, 'main/info/credit.html', {'title': 'Кредит и рассрочка'})

def bonus(request):
    return render(request, 'main/info/bonus.html', {'title': 'Бонусная программа'})

def privacy(request):
    return render(request, 'main/info/privacy.html', {'title': 'Политика конфиденциальности'})

def terms(request):
    return render(request, 'main/info/terms.html', {'title': 'Пользовательское соглашение'})

def public_offer(request):
    return render(request, 'main/info/public_offer.html', {'title': 'Публичная оферта'})

def contacts(request):
    return render(request, 'main/info/contacts.html', {'title': 'Контакты'})

def faq(request):
    return render(request, 'main/info/faq.html', {'title': 'Частые вопросы'})

def vacancies(request):
    return render(request, 'main/info/vacancies.html')

def partners(request):
    return render(request, 'main/info/partners.html')
