from rest_framework import generics

from cafeterias.cafeterias_models.orders import OrderItem
from cafeterias.api.serializers import OrderItemSerializer


class OrderItems(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    