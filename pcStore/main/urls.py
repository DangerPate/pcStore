from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', include('catalog.urls')),
    path('delivery/', views.delivery, name='delivery'),
    path('warranty/', views.warranty, name='warranty'),
    path('returns/', views.returns, name='returns'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('public-offer/', views.public_offer, name='public_offer'),
    path('faq/', views.faq, name='faq'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('partners/', views.partners, name='partners'),
]