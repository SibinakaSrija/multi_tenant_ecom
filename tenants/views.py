# tenants/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
def vendor_health(request):
    """
    Simple health/check endpoint to confirm route is working on GET.
    """
    return Response({"message": "Vendors endpoint alive"}, status=status.HTTP_200_OK)
