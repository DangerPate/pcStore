from django.urls import path
from . import views
urlpatterns = [
    path('', views.mini_product_card, name='mini_product_card')
]