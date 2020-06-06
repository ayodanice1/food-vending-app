from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .api.apiviews import *


app_name = 'cafeterias'

urlpatterns = [
    path('menus/', MenuList.as_view(), name='menu_list'),
    path('menus/add/', csrf_exempt(MenuCreate.as_view()), name='add_menu'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu_detail'),
    path('menus/<int:pk>/update/', csrf_exempt(MenuUpdate.as_view()), name='menu_update'),
    path('menus/<int:pk>/purchase/', csrf_exempt(MenuPurchase.as_view()), name='menu_purchase'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', csrf_exempt(OrderDetail.as_view()), name='check_cancel_order'),
    path('orders/<int:pk>/checkout/', csrf_exempt(OrderCheckout.as_view()), name='order_checkout'),
    path('orders/open/', OrderCreate.as_view(), name='new_order'),
    path('orders/addorderitems/', OrderItems.as_view(), name='order_items'),
    path('sales/', salesReportView, name='sales_report'),
]
