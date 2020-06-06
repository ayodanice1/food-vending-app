from rest_framework import serializers
from rest_framework.authtoken.models import Token

from ..models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'email', 'phone_number', 'is_vendor', 'business_name', 'first_name', 'last_name', 'outstanding' )
            

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'email', 'phone_number', 'first_name', 'last_name', 'password' )
        
    def create(self, validated_data): 
        user = User.objects.create_user(
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            password=self.validated_data['password'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.save()
        Token.objects.create(user=user)
        return user


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'email', 'phone_number', 'business_name', 'password' )
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            password=self.validated_data['password'],
            business_name=self.validated_data['business_name'],
            is_vendor=True
        )
        user.save()
        Token.objects.create(user=user)
        return user

