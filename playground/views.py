from django.shortcuts import render
from django.http import HttpResponse


def HelloWorld (request):  
    return render(request, 'hello.html', {'name': 'World'})





# Create your views here.
# request -> reponse
# request handler
# action 