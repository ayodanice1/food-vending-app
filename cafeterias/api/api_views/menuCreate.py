from rest_framework import generics

from cafeterias.permissions import IsVendor
from cafeterias.api.serializers import MenuSerializer


class MenuCreate(generics.CreateAPIView):
    permission_classes = ( IsVendor, )
    
    serializer_class = MenuSerializer
    