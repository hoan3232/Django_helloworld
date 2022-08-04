from django.urls import path
from . import views

urlpatterns = [
    path('Cart/', views.Cart, name='cart'),
    path('CheckOut/', views.CheckOut, name='checkout'),
    path('Store/', views.Store, name='store'),
    path('update_item/', views.updateItem, name="update_item"),
    path('<slug:slug>/', views.post_comment, name='post_commnent')
]