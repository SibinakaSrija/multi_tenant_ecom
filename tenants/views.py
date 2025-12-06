# tenants/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import Vendor
from .serializers import VendorSerializer

@api_view(['GET', 'POST'])
def vendors_list_create(request):
    """
    GET  -> list all vendors
    POST -> create a vendor with JSON payload {name, contact_email, domain}
    """
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])   # 👈 ADD THIS
def vendor_health(request):
    return Response({"message": "Vendors endpoint alive"}, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=404)

    if request.method == "GET":
        return Response(VendorSerializer(vendor).data)

    if request.method == "PUT":
        s = VendorSerializer(vendor, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)

    if request.method == "DELETE":
        vendor.delete()
        return Response(status=204)
