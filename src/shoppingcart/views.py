from itertools import product
from multiprocessing import context
from re import template
from webbrowser import get
from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.core.paginator import Paginator
from .forms import *


# Create your views here.

def Store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store.html', context)

def shop(request, type, content, page, nomatch):
    name = content
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if type == "category":
        if content == "All":
            products = Product.objects.all()
            name = 'All books'
        else:
            products = Product.objects.filter(category = content)
    elif type == "author":
        products = Product.objects.filter(author = content)    
    elif type == "price":
        if content == "lt2":
            products = Product.objects.filter(price__lt=200.000)
            name = 'Less than 200.000 VND'
        elif content == "gt3":
            products = Product.objects.filter(price__gt=300.000)
            name = 'Greater than 300.000 VND'
        elif content == "r23":
            products = Product.objects.filter(price__range=[200.000, 300.000])
            name = '200.000 - 300.000 VND'
    
    paginator = Paginator(products, 12)
    page_count = paginator.num_pages
    page_obj = paginator.get_page(page)

    if page > 3:
        i = page -2
    else:
        i = 1
    context = {'title':'Shop', 'products':page_obj, 'name':name, 'cartItems':cartItems, 'pages': page_count, 'current' :page, 'i' : i, 'range' : range(i, page + 3), 'nomatch': nomatch}
    return context

def shop_category(request, type, content):
    name = content
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if type == "category":
        if content == "All":
            products = Product.objects.all()
            name = 'All books'
        else:
            products = Product.objects.filter(category = content)
    elif type == "author":
        products = Product.objects.filter(author = content)    
    elif type == "price":
        if content == "lt2":
            products = Product.objects.filter(price__lt=200.000)
            name = 'Less than 200.000 VND'
        elif content == "gt3":
            products = Product.objects.filter(price__gt=300.000)
            name = 'Greater than 300.000 VND'
        elif content == "r23":
            products = Product.objects.filter(price__range=[200.000, 300.000])
            name = '200.000 - 300.000 VND'

    context = {'title':'Shop', 'products':products, 'name':name, 'cartItems':cartItems}
    return context




def Shop_category_render(request, type, content):
    return render(request, 'shop.html', shop_category(request, type, content))

def Shop_render_all(request):
    return render(request, 'shop.html', shop(request, 'category', 'All', 1, 0))

def Shopall_pagination(request, page):
    return render(request, 'shop.html', shop(request, 'category', 'All', page, 0))


def Details(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    stock = Stock.objects.get(id = id).instock
    product = get_object_or_404(Product, id=id)
    products = Product.objects.filter(category = product.category)[:6]
    context = {'title':'Details', 'product':product, 'cartItems':cartItems, 'products':products, 'stock':stock}
    return render(request, 'details2.html', context)

def Home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    product1 = get_object_or_404(Product, id=2)
    product2 = get_object_or_404(Product, id=3)
    product3 = get_object_or_404(Product, id=4)

    type = ['Fiction', 'Poetry', 'Self-Help', 'Social Science']
    category_list = []
    for category in type:
        category_ = {'products': Product.objects.filter(category__startswith=category), 'category':category}
        category_list.append(category_)

    context={'title':'Home', 'product1':product1, 'product2':product2, 'product3':product3, 'categories':category_list, 'cartItems':cartItems}
    return render(request, 'home.html', context)

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']  

    intsock = []
    instock = [0 for i in range(len(items))]
    k = 0
    for i in items:
        instock[k] =  Stock.objects.get(id=i.id).quantity
        k += 1

    zipped = zip(items,instock)

    context =  {'title':'Cart', 'zip':zipped, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)

def CheckOut(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'title':'Checkout', 'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'checkout.html', context)

def About(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'title':'About', 'cartItems':cartItems}
    return render(request, 'about.html', context)

def search_product(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if request.method == "POST":
        query_name = request.POST.get('name', None)
        title = 'Result for: ' + query_name
        if query_name:
            products = Product.objects.filter(name__contains=query_name)
            context =  {'title':title, "products":products, "cartItems":cartItems}
            return render(request, 'shop.html', context)

    return render(request, 'shop.html')

def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']

    print(productID)
    print(action)

    customer = request.user.customer
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, price=product.price)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    print('Data:', request.body)
    transactionID = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transactionID

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                sub_district=data['shipping']['sub_district'],
                district=data['shipping']['district']
            )
    else:
        print('Not authen user')

    return JsonResponse('Payment done', safe=False)
