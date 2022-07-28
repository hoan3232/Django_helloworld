from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.http import JsonResponse


# Create your views here.

def Store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store.html', context)

def Cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}    

    context =  {'title':'Cart', 'items':items, 'order':order}
    return render(request, 'cart.html', context)

def CheckOut(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}    

    context = {'title':'Checkout', 'items':items, 'order':order}
    return render(request, 'checkout.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)
