from django.urls import path
from App_Payment.views import checkout, payment, complete

app_name = 'App_Payment'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('pay/', payment, name='payment'),
    path('status/',complete, name='complete')
]
