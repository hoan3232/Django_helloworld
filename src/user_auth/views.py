import django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from shoppingcart.models import Customer, Product

# Create your views here.

def signin_user(request, place):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if place == 0:
                return redirect('home')
            else:
                return redirect('details', place)
        else:
            #aaaaaa
            messages.success(request,("Login failled, please try again"))
            return redirect('signin', 0)
    else:
        return render(request, 'signin.html', {})

def signup_user(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cfmpassword']
        
        user = User.objects.create_user(username,email,password2)
        user.first_name = fname
        user.last_name = lname
        user.save()

        user1 = User.objects.get(username = username)



        customer = Customer.objects.create()
        customer.user = user1
        customer.name = username
        customer.email = email
        customer.save()
        

        
        return redirect('signin', 0)

    return render(request,'signup.html',{})


def logout_user(request):
    logout(request)
    return redirect('home')