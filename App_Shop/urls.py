from django.urls import path
from App_Shop.views import Home, ProdcuctDetail

app_name = 'App_Shop'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<int:pk>/', ProdcuctDetail.as_view(), name='product_detail',)

]