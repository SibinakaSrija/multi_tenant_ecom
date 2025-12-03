from django.http import JsonResponse
from .models import Order, OrderItem
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
import json

def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
