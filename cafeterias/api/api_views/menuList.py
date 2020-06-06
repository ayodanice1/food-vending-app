from rest_framework.response import Response
from rest_framework.views import APIView

from cafeterias.cafeterias_models.menus import Menu
from cafeterias.api.serializers import MenuSerializer


class MenuList(APIView):
    def get(self, request):
        user = request.user
        if user.is_vendor:
            queryset = Menu.objects.filter(vendor=user.id)
        else:
            queryset = Menu.objects.all()
        data = MenuSerializer(queryset, many=True).data
        return Response(data)
    