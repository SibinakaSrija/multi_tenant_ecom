from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from core.permissions import IsStoreOwner, IsVendorStaff

@api_view(['GET', 'POST'])
def product_list_create(request):
    vendor = request.tenant
    if vendor is None:
        return Response({"error": "Tenant not found"}, status=400)

    if request.method == "GET":
        products = Product.objects.filter(vendor=vendor)
        return Response(ProductSerializer(products, many=True).data)

    data = request.data.copy()
    data['vendor'] = vendor.id

    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    vendor = request.tenant
    if vendor is None:
        return Response({"error": "Tenant missing"}, status=400)

    try:
        product = Product.objects.get(pk=pk, vendor=vendor)
    except Product.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == "GET":
        return Response(ProductSerializer(product).data)

    if request.method == "PUT":
        s = ProductSerializer(product, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)

    if request.method == "DELETE":
        product.delete()
        return Response(status=204)
f

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        tenant = getattr(self.request, 'tenant', None)
        if not tenant:
            return Product.objects.none()
        return Product.objects.filter(vendor=tenant)

    def perform_create(self, serializer):
        tenant = getattr(self.request, 'tenant', None)
        serializer.save(vendor=tenant)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]       # Public view
        return [IsAuthenticated()]    # Create/edit/delete → login required
