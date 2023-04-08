from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib import messages
from django.urls import reverse
from App_Order.models import Order
from App_Payment.forms import BillingForm
from App_Payment.models import BillingAddress
# for payment
# from sslcommerz_lib import SSLCOMMERZ
from decimal import Decimal
import socket

from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # print(order_qs)
    order_items = order_qs[0].orderitems.all()
    # print(order_items)
    order_total = order_qs[0].get_totals()
    return render(request,'App_Payment/checkout.html', context={"form":form, "order_items":order_items, 'order_total': order_total, 'saved_address':saved_address})

@login_required
def payment(request, *args, **kwargs):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled():
        messages.info(request, f"Please complete your shipping address")
        return redirect('App_Payment:checkout')
    if not request.user.profile.is_fully_field():
        messages.info(request, "Please complete your profile details")
        return redirect('App_Login:profile')
    return render(request, "App_Payment/payment.html", context={})
@login_required
def complete(request, *args, **kwargs):
    render(request, 'App_Payment/complete.html', context={})
