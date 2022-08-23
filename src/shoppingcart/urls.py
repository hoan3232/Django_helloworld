from django.urls import path
from . import views

urlpatterns = [
    path('Cart/', views.Cart, name='cart'),
    path('CheckOut/', views.CheckOut, name='checkout'),
    path('Store/', views.Store, name='store'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    #path('<slug:slug>/', views.post_comment, name='post_commnent'),
    path('Details/<int:id>', views.Details, name='details'),
    path('Home/', views.Home, name='home'),
    path('Shop/<str:type>/<str:content>', views.Shop, name='shop')
]