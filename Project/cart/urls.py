from django.urls import path
from . import views



urlpatterns = [
    path('cart-add/<int:id>', views.cart_add, name='cart_add'),
    path('cart-add-sepet/<int:id>', views.cart_add_sepet, name='cart_add_sepet'),
    path('cart-detail', views.cart_detail, name='cart_detail'),
    path('cart-remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('cart-remove-sepet/<int:id>', views.cart_remove_sepet, name='cart_remove_sepet')

]
