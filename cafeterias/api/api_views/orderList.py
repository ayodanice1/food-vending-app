from rest_framework.views import APIView
from rest_framework.response import Response

from cafeterias.cafeterias_models.orders import Order
from cafeterias.api.serializers import OrderSerializer


class OrderList(APIView):
    
    def get(self, request):
        user = request.user
        if user.is_vendor:
            orders = Order.objects.filter(vendor=user)
        else:
            orders = Order.objects.filter(customer=user)
        data = OrderSerializer(orders, many=True).data
        return Response(data)
    