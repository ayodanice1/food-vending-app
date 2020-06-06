from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Menu, Order, OrderItem
from cafeterias.cafeterias_models.menus import Day



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ( 'id', 'name', 'description', 'quantity', 'vendor', 'price', 'scheduled_days' )
        
    def create(self, validated_data): 
        scheduled_days=self.validated_data['scheduled_days']
        menu = Menu.objects.create(
            name=self.validated_data['name'],
            description=self.validated_data['description'],
            quantity=self.validated_data['quantity'],
            vendor=self.validated_data['vendor'],
            price=self.validated_data['price'],
        )
        menu.save()
        for scheduled_day in scheduled_days:
            menu.scheduled_days.add(Day.objects.get(name=scheduled_day))
        return menu
    
class MenuPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ( 'id', 'quantity' )
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( 'id', 'customer', 'vendor', 'total_order_cost', 
            'amount_paid', 'outstanding', 'order_status', 'payment_status', 'time_created' )
        
    def create(self, validated_data): 
        order = Order.objects.create(
            customer=self.validated_data['customer'],
            vendor=self.validated_data['vendor'],
        )
        order.save()
        return order
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ( 'id', 'order', 'item', 'quantity', 'order_cost' )
        
    def create(self, validated_data): 
        order_item = OrderItem.objects.create(
            order=self.validated_data['order'],
            item=self.validated_data['item'],
            quantity=self.validated_data['quantity'],
        )
        order_item.save()
        return order_item
    
class OrderCheckoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ( 'id', 'total_order_cost', 
            'amount_paid', 'outstanding', 'order_status', 'payment_status' )
    
