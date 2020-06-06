from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics

from cafeterias.cafeterias_models.orders import OrderItem
from cafeterias.api.serializers import OrderItemSerializer


class OrderItemDetail(generics.RetrieveDestroyAPIView):
    def get(self, request, pk):
        order_item = get_object_or_404(OrderItem, pk=pk)
        data = OrderItemSerializer(order_item).data

        return Response(data)
    