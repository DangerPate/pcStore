from django.shortcuts import render
from catalog.models import Product, Category
def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

def about(request):
    return render(request, 'main/about.html')