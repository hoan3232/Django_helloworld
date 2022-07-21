from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('HelloWorld/', views.HelloWorld),
    path('Test/', views.Test),
]