from django.db import models
from django.shortcuts import get_object_or_404

from .menus import Menu

import users


class Order(models.Model):
    ORDER_STATUS_CHOICES=(
        ('NEW', 'New Order'), ('NEW-PURCHASE', 'New Purchase Order'), ('RECEIVED', 'Order Received'),
        ('READY', 'Order Ready'), ('DELIVERED', 'Order Delivered'), 
        ('CANCEL-REQUESTED', 'Order Cancelling requested'), ('CANCELLED', 'Order Cancelled'), )
    PAYMENT_STATUS_CHOICES=(
        ('NOT-PAID', 'Not yet paid for'), ('PART-PAID', 'Partly paid for'), ('FULLY-PAID', 'Fully paid for'), )
    
    customer = models.ForeignKey( 
        'users.User', on_delete=models.CASCADE, limit_choices_to={'is_vendor':False},
        related_name='orders', blank=True, null=True )
    vendor = models.ForeignKey( 
        'users.User', on_delete=models.CASCADE, limit_choices_to={'is_vendor':True},
        related_name='sells', blank=True, null=True )
    total_order_cost = models.DecimalField( verbose_name='Total Order Cost', max_digits=10, decimal_places=2, default=0.0 )
    amount_paid = models.DecimalField( verbose_name='Amount Paid', max_digits=10, decimal_places=2, default=0.0 ) 
    outstanding = models.DecimalField( max_digits=10, decimal_places=2, default=0.0 ) 
    time_created = models.DateTimeField( auto_now_add=True )
    order_status = models.CharField( max_length=20, choices= ORDER_STATUS_CHOICES, default='NEW' )
    payment_status = models.CharField( max_length=10, choices= PAYMENT_STATUS_CHOICES, default='NOT-PAID' )
    
    class Meta:
        ordering = ['-time_created']
    
    def __str__(self):
        return f"{self.customer} ({self.order_status})"
    
class OrderItem(models.Model):
    order = models.ForeignKey( 'Order', on_delete=models.CASCADE, blank=True, null=True )
    item = models.ForeignKey( 'Menu', on_delete=models.SET_NULL, blank=True, null=True )
    quantity = models.PositiveIntegerField( default=1 )
    order_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"{self.order} ({self.id})"
    
    def _set_order_cost(self):
        return float(self.item.price) * int(self.quantity)
    
    def save(self, *args, **kwargs):
        self.order_cost = self._set_order_cost()
        order = Order.objects.get(pk=self.order.id)
        super().save(*args, **kwargs)

