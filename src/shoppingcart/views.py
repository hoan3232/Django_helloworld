from multiprocessing import context
from re import template
from webbrowser import get
from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import JsonResponse
from .forms import *

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


def post_comment(request, slug): 
    template = ''
    post = get_object_or_404(Product, slug=slug)
    comments = post.comments.filter(active=True)

    ew_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})