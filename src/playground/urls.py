from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('shop/', views.HelloWorld),
    
]