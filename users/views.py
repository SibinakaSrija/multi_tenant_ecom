from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
