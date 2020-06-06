from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied

from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import NotificationSerializer

from notifications.models import Notification
from users.api.serializers import UserSerializer
from notifications.api.serializers import NotificationCreateSerializer
from users.models import User



class NotificationList(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(sender=user)
        data = { 'profile': UserSerializer(user).data }
        if not notifications:
            notifications = Notification.objects.filter(receiver=user)
            if not notifications:
                data['message'] = 'No notifications found.'
            else:
                data['notifications'] = NotificationSerializer(notifications, many=True).data
        else:
            data['notifications'] = NotificationSerializer(notifications, many=True).data
        return Response( data )
    
class NotificationDetail(generics.RetrieveAPIView):
    def get(self, request, pk):
        user = request.user
        notification = get_object_or_404(Notification, pk=pk)
        data = { 'profile': UserSerializer(user).data }
        if notification.receiver == user:
            notification.message_status='READ'
            notification.save()
            data['notification'] = NotificationSerializer(notification).data
        elif notification.sender == user:
            data['notification'] = NotificationSerializer(notification).data
        else:
            data['error'] = 'Permission denied' 
        return Response(data)
    
class NotificationCreate(generics.CreateAPIView):
    serializer_class = NotificationCreateSerializer
    
    def post(self, request):
        user = request.user
        receiver = request.POST.get('receiver')
        
        if int(receiver) == user.id:
            data = { 'error': 'You cannot message yourself.' }
        else:
            notification = Notification.objects.create(
                sender=user,
                receiver=User.objects.get(pk=receiver),
                subject=request.POST.get('subject'),
                body=request.POST.get('body')
            )
            notification.save()
            data = NotificationSerializer(notification).data
            data['message'] = 'Notification sent.'
        return Response(data)
