from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from App_Shop.models import Product
# mixin
from django.contrib.auth.mixins import LoginRequiredMixin
class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProdcuctDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'


