from multiprocessing import context
from django.shortcuts import render
from .models import *


# Create your views here.

def Store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)

def Cart(request):
    context =  {'title': 'Cart'}
    return render(request, 'cart.html', context)

def CheckOut(request):
    context = {'title': 'Checkout'}
    return render(request, 'checkout.html', context)