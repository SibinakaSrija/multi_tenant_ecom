from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer

@api_view(['POST'])
def create_order(request):
    vendor = request.tenant
    if vendor is None:
        return Response({"error": "Tenant missing"}, status=400)

    items = request.data.get("items", [])
    order = Order.objects.create(vendor=vendor, customer=request.user)

    total = 0
    for item in items:
        OrderItem.objects.create(
            order=order,
            product_id=item["product"],
            quantity=item["qty"],
            price=item["price"]
        )
        total += item["qty"] * float(item["price"])

    order.total = total
    order.save()

    return Response(OrderSerializer(order).data, status=201)

@api_view(['GET'])
def list_orders(request):
    vendor = request.tenant
    orders = Order.objects.filter(vendor=vendor)
    return Response(OrderSerializer(orders, many=True).data)
