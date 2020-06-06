from django.contrib import admin

from .models import Day, Menu, Order, OrderItem

# Register your models here.
admin.site.register(Day)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
