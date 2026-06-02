from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_index, name='catalog_index'),
    path('search/', views.search_view, name='search'),
    path('<slug:category_slug>/', views.category_view, name='category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:slug>/review/', views.add_review, name='add_review'),
    path('review/vote/', views.toggle_vote, name='toggle_vote'),
    path('review/comment/', views.add_comment, name='add_comment'),
    path('promotion/<slug:promotion_slug>/', views.promotion_view, name='promotion'),
]