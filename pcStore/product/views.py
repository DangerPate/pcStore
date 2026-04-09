from django.shortcuts import render

def mini_product_card(request):
    return render(request, 'product/mini_product_card.html')
