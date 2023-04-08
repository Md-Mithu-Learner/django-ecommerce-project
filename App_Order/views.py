from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from App_Order.models import Cart, Order
from App_Shop.models import Product
from django.contrib import messages


@login_required
def add_to_cart(request, pk, *args, **kwargs):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    print(order_item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print(order_qs)

    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This Quantity Was Updated.")
            return redirect("App_Shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This Is Was Added To Your Cart.")
            return redirect("App_Shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "THIS ITEM WAS ADDED TO YOUR CART.")
        return redirect("App_Shop:home")

@login_required
def cart_view(request, *args, **kwargs):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order=orders[0]
        return render(request, 'App_Order/cart.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "You Don't Have Any Item In Your Cart")
        return redirect("App_Shop:home")
@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from your cart")
            return redirect('App_Order:cart')
        else:
            messages.info(request, "This item was not in your card")
            return redirect('App_Shop:home')
    else:
        messages.info(request, "YOU DON`T HAVE AN ACTIVE ORDER")
        return redirect("App_Shop:home")
@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("App_Shop:home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_Shop:home")


@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} item has been removed from your cart")
                return redirect("App_Order:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("App_Shop:home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_Shop:home")