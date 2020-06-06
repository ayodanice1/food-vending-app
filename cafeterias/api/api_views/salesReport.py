from django.db.models.aggregates import Sum
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import User
from cafeterias.cafeterias_models.orders import Order
from users.api.serializers import UserSerializer


@api_view()
def salesReportView(request):
    user = request.user
    data = {}
    if not user.is_vendor:
        data['error'] = 'Permission denied. User must be a vendor.' 
    else:
        today = timezone.now()
        vendor = User.objects.get(pk=user.id)
        print(today.date())
        orders = Order.objects.filter(vendor=vendor, time_created__startswith=today.date())
        if not orders:
            data['message'] = 'No sales for today.' 
        else:
            data['profile'] = UserSerializer(user).data
            data['message'] = f'Sales Record for today, {timezone.now().date()}'
            data['number_of_orders'] = orders.count()
            data['today_sales_record'] = [ 
                orders.aggregate(Sum('total_order_cost')), 
                orders.aggregate(Sum('amount_paid')), 
                orders.aggregate(Sum('outstanding')),
            ]
    return Response(data)
    
