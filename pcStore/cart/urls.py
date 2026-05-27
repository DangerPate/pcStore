from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/toggle/<slug:product_slug>/', views.toggle_favorite, name='toggle_favorite'),
    path('bulk-action/', views.bulk_cart_action, name='bulk_action'),  # 🔑 Массовые действия
    path('checkout/', views.checkout_selected, name='checkout'),
]