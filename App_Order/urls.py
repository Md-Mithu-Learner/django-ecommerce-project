from django.urls import path
from App_Order.views import add_to_cart, cart_view, remove_from_cart,increase_cart,decrease_cart

app_name = 'App_Order'

urlpatterns = [
    path('add/<pk>/', add_to_cart, name="add"),
    path('cart/', cart_view, name="cart"),
    path('remove/<pk>/', remove_from_cart, name="cart_remove"),
    path('increase/<pk>/', increase_cart, name="increase"),
    path('decrease/<pk>/', decrease_cart, name="decrease"),
]