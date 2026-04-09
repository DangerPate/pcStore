from django.shortcuts import render
from product.models import Product
def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

def about(request):
    return render(request, 'main/about.html')