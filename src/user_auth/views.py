import django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def signin_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,("Login successfully"))
            return redirect('signin')
        else:
            messages.success(request,("Login failled, please try again"))
            return redirect('signin')
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
        return redirect('signin')

    return render(request,'signup.html',{})


def logout_user(request):
    logout(request)
    #return redirect('home')