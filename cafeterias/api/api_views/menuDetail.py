from rest_framework import generics

from cafeterias.permissions import IsConcerned
from cafeterias.cafeterias_models.menus import Menu
from cafeterias.api.serializers import MenuSerializer


class MenuDetail(generics.RetrieveAPIView):
    permission_classes = ( IsConcerned, )
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
