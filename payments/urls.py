from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='payments-home'),
    path('webhook/', views.coinbase_webhook),
]
