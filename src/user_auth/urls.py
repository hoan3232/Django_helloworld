import imp

from django.urls import path
from . import views

urlpatterns = [
    path('signin_user',views.signin_user, name="signin"),
]