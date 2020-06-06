from django.shortcuts import render
from django.http.response import JsonResponse

from users.models import User


def index(request):
    user = request.user
    if not user.is_authenticated:
        context = { 'message' : 'Welcome on board' }
        return render(request, 'index.html', context)
    else:
        user = User.objects.get(pk=user.id)
        return JsonResponse({ 'message' : 'You are logged in already. Go to /api/login/ for more instructions.' })
    