from rest_framework import generics
from rest_framework.response import Response

from cafeterias.permissions import IsCustomer
from cafeterias.cafeterias_models.menus import Menu
from cafeterias.api.serializers import MenuPurchaseSerializer, OrderItemSerializer
from cafeterias.cafeterias_models.orders import Order, OrderItem
from users.models import User
from utils.cafeteriaUtils import get_today_name


class MenuPurchase(generics.RetrieveAPIView):
    permission_classes = ( IsCustomer, )
    
    queryset = Menu.objects.all()
    serializer_class = MenuPurchaseSerializer
    
    def post(self, request, pk):
        menu_item = Menu.objects.get(pk=pk)
        customer = User.objects.get(pk=request.user.id)
        vendor = User.objects.get(pk=menu_item.vendor.id)
        quantity = request.POST.get('quantity')
        today = get_today_name()
        if not today in [day.name for day in menu_item.scheduled_days.all()]:
            data = { 'error' : 'Menu item is not scheduled for today.' }
        else:
            order=Order.objects.create(customer=customer, vendor=vendor)
            new_purchase = OrderItem.objects.create(
                order=order,
                item=menu_item,
                quantity=quantity,
            )
            new_purchase.save()
            order.total_order_cost = order.outstanding = order.total_order_cost + new_purchase.order_cost
            order.save()
            order.order_status = 'NEW-PURCHASE'
            order.save()
            customer.outstanding = float( customer.outstanding ) + float(order.total_order_cost)
            customer.save()
            data = OrderItemSerializer(new_purchase).data
            data['next-step'] = f'Proceed to /api/orders/{order.id}/checkout/'
        return Response(data)
