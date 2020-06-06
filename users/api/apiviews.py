from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout

from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import User

from .serializers import ( UserSerializer, CustomerSerializer, VendorSerializer )
from users.api import serializers
from cafeterias.permissions import IsCustomer, IsVendor


class LoginView(View):
    
    api_endpoints = {
        'GET /api/users/' : 'View list of users on the app. Admin-only access.',
        'GET /api/users/<int:pk>/' : 'View a user detail. Admin-only access.',
        'GET /api/vendors/' : 'View list of vendors only. Customer-only access.',
        'GET /api/vendors/<int:pk>/': 'View a vendor detail. Customer-only access.',
        'POST /api/vendors/register/': 'Register a new vendor.',
        'GET/api/customers/': 'View list of customers only. Vendor-only access.',
        'GET /api/customers/<int:pk>/': 'View a customer detail. Vendor-only access.',
        'POST /api/customers/register/': 'Register a new customer.',
        'GET /api/sales/': 'Get daily sales records.',
        'GET /api/menus/': 'View list of available menus.',
        'GET /api/menus/<int:pk>/': 'View a menu detail.',
        'PUT /api/menus/<int:pk>/update/': 'Update a menu item detail.',
        'POST /api/menus/<int:pk>/purchase/': 'Purchase a menu item.',
        'POST /api/menus/add/': 'Add new menu item.',
        'GET /api/orders/': 'View list of orders.',
        'GET-POST-DELETE /api/orders/': 'View-Update-Cancel an order.',
        'POST /api/orders/<int:pk>/checkout/': 'Pay for an order.',
        'GET /api/notifications/': 'View list of notifications received and sent.',
        'GET /api/notifications/<int:pk>/': 'View a notification.',
        'POST /api/notifications/send/': 'Send a notification.',
    }
    
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({ 'message' : 'You are already logged in.', 'APIS' : self.api_endpoints })
        else:
            return render(request, 'index.html', { 'message' : 'Come onboard with us, pal.' })
    
    def post(self, request,):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            data = UserSerializer(user).data
            data['message'] = 'Login successful'
            data['APIs'] = self.api_endpoints
            return JsonResponse(data)
        else:
            return render(request, 'index.html', { 'message' : 'Wrong credentials.' })
            #return JsonResponse({ "error": "Wrong Credentials" }, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        return self.post(request)
    
    def post(self, request):
        logout(self.request)
        return render(request, 'index.html', { 'message' : 'Successful logout.' })

class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser, )
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser, )
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class VendorList(generics.ListAPIView):
    permission_classes = ( IsCustomer, )
    
    queryset = User.objects.all()
    serializer_class = VendorSerializer
    
class VendorDetail(generics.RetrieveAPIView):
    permission_classes = (IsCustomer, )
    
    queryset = User.objects.all()
    serializer_class = VendorSerializer
    
class VendorCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    
    serializer_class = VendorSerializer
    
class CustomerList(generics.ListAPIView):
    permission_classes = ( IsVendor, )
    
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveAPIView):
    permission_classes = (IsVendor, )
    
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    
    serializer_class = CustomerSerializer
    
