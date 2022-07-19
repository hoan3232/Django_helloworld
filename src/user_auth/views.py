import django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            return redirect('signin')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',{})