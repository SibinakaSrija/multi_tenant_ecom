# tenants/serializers.py
from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_email', 'domain', 'created_at']
        read_only_fields = ['id', 'created_at']
