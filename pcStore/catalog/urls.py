from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('<slug:category_slug>/', views.category_view, name='category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]