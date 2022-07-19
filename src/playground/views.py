from django.shortcuts import render
from django.http import HttpResponse

from playground.models import Customer


def HelloWorld (request):
    customers = Customer.objects.all()
    return render(request, 'hello.html', {'customers': customers})

def Test (request):
    return render(request, 'Lab2.html')

def SignUp (request):
    return render(request, 'signup.html')

def SignIn (request):
    return render(request, 'signin.html')
    





# Create your views here.
# request -> reponse
# request handler
# action 