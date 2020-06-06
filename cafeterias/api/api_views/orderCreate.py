from rest_framework import generics

from cafeterias.api.serializers import OrderSerializer
from cafeterias.permissions import IsCustomer


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    
    permission_classes = ( IsCustomer, )
    
