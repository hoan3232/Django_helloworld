import imp

from django.urls import path
from . import views

urlpatterns = [
    path('signin_user/<int:place>',views.signin_user, name="signin"),
    path('signup_user',views.signup_user, name="signup"),
    path('logout_user',views.logout_user, name="logout")
]