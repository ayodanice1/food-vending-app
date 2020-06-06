from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from rest_framework_swagger.views import get_swagger_view

from .api.apiviews import NotificationList, NotificationDetail, NotificationCreate


app_name = 'notifications'

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='view_notifications'),
    path('notifications/send/', csrf_exempt(NotificationCreate.as_view()), name='view_notifications'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(), name='notification_detail'),
]