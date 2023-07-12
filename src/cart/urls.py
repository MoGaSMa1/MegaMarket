from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('cart_add/<int:pk>', views.cart_add, name='cart_add'),
    path('cart_remove/<int:pk>', views.cart_remove, name='cart_remove'),
]