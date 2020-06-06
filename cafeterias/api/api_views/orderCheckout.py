from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics

from cafeterias.permissions import IsOrderOwner
from cafeterias.cafeterias_models.orders import Order
from cafeterias.api.serializers import OrderCheckoutSerializer, OrderSerializer

from users.models import User


class OrderCheckout(generics.RetrieveAPIView):
    permission_classes = ( IsOrderOwner, )
    
    queryset = Order.objects.all()
    serializer_class = OrderCheckoutSerializer
    
    # Pay for the order
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        customer = User.objects.get(pk=request.user.id)
        amount_paid = float( request.POST.get('amount_paid') )
        
        customer.outstanding = float( customer.outstanding ) - amount_paid
        customer.save()
        
        if amount_paid >= float( order.outstanding ):
            order.outstanding = float( order.outstanding ) - amount_paid
            order.save()
            if order.order_status == 'CANCEL-REQUESTED':
                order.order_status = 'CANCELLED'
                order.save()
                order.payment_status = 'FULLY-PAID'
                order.save()
            elif amount_paid >= float( order.total_order_cost ):
                order.payment_status = 'FULLY-PAID'
                order.save()
            else:
                order.payment_status = 'PART-PAID'
                order.save()
            data = OrderSerializer(order).data
        elif order.order_status == 'CANCEL-REQUESTED':
            data = { 'message' : 'Cannot complete transaction due to underpayment.' }
        elif amount_paid > 1:
            order.outstanding = float( order.outstanding ) - amount_paid
            order.save()
            order.payment_status = 'PART-PAID'
            order.save()
        return Response(data)
            
    
