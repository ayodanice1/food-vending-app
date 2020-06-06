from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from rest_framework import generics
from rest_framework.response import Response

from cafeterias.permissions import IsConcerned
from cafeterias.cafeterias_models.orders import Order
from cafeterias.api.serializers import OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    permission_classes = ( IsConcerned, )
    
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer
    
    # Update the order status. By the vendor
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        
        if request.user.is_vendor:
            order_status = request.data.get('order_status')
            if order_status != None:
                order.order_status = order_status
                order.save()
                return Response(OrderSerializer(order).data)
            else:
                return Response({'error' : 'New order status is not specified.'})
        else:
            "Customers have no right to update an order status"
            raise PermissionDenied
        
    # Cancel the order. By the customer
    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        
        if not request.user.is_vendor:
            if order.order_status == 'NEW' or 'RECEIVED' or 'CANCEL-REQUESTED':
                order.order_status = 'CANCEL-REQUESTED'
                order.save()
                # Damages due on cancellation is 40% of tiotal order cost
                order.outstanding = float(order.total_order_cost) * 0.4
                order.save()
                data = { 
                    'order' : OrderSerializer(order).data,
                    'next-step' : f'Proceed to api/orders/{order.id}/checkout/ to complete this transaction.'
                }
                return Response(data)
            elif order.order_status in ('NEW-PURCHASE', 'READY', 'DELIVERED', 'CANCELLED', 'eCANCEL-REQUESTED'):
                return Response({ 'message' : 'This order cannot be cancelled.' })
        else:
            "Vendors have no right to update an order status"
            raise PermissionDenied
        