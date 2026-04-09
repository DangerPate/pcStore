from django.shortcuts import render
from .models import Product
def mini_product_card(request):
    products = Product.objects.all()
    return render(request, 'product/mini_product_card.html', {'products': products})
