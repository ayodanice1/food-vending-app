from rest_framework import generics

from cafeterias.permissions import IsMenuOwner
from cafeterias.cafeterias_models.menus import Menu
from cafeterias.api.serializers import MenuSerializer


class MenuUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = ( IsMenuOwner, )
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    