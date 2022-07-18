from django.shortcuts import render
from django.http import HttpResponse


def HelloWorld (request):  
    return render(request, 'hello.html', {'name': 'World'})

def Test (request):
    return render(request, 'Lab2.html')
    





# Create your views here.
# request -> reponse
# request handler
# action 