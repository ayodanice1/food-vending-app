from rest_framework import serializers

from ..models import Notification



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ( 'id', 'sender', 'receiver', 'subject', 'body', 'message_status' )
        
class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ( 'receiver', 'subject', 'body' )

