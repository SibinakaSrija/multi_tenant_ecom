from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
import json

def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
