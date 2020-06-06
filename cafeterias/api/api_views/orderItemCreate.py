from rest_framework import generics

from cafeterias.permissions import IsCustomer
from cafeterias.api.serializers import OrderItemSerializer


class OrderItemCreate(generics.CreateAPIView):
    permission_classes = ( IsCustomer, )
    
    serializer_class = OrderItemSerializer
    