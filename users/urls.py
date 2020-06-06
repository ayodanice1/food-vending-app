from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .api.apiviews import (
    VendorList, VendorCreate, VendorDetail, CustomerList, UserList,
    CustomerCreate, CustomerDetail, LoginView, LogoutView, UserDetail,
)


app_name = 'users'

urlpatterns = [
    path('login/', csrf_exempt(LoginView.as_view()), name='login'),
    path('logout/', csrf_exempt(LogoutView.as_view()), name='logout'),
    path('users/', UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('vendors/', VendorList.as_view(), name='users_list'),
    path('vendors/register/', VendorCreate.as_view(), name='vendors_create'),
    path('vendors/<int:pk>/', VendorDetail.as_view(), name='vendors_detail'),
    path('customers/', CustomerList.as_view(), name='customers_list'),
    path('customers/register/', CustomerCreate.as_view(), name='customer_create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customers_detail'),
]

