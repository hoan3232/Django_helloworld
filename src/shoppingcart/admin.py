from django.contrib import admin
from .models import Customer, Order, Product, ShippingAddress, OrderItem
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)