# core/middleware.py
from django.http import JsonResponse
from vendors.models import Vendor   # Use the correct location of your Vendor model

class TenantMiddleware:
    """
    Extract tenant from X-Tenant-Domain header or subdomain
    and attach it to request.tenant
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Try to read from header
        domain = request.META.get('HTTP_X_TENANT_DOMAIN')  # Django converts headers to META with HTTP_

        # 2. If not found, try to read subdomain
        if not domain:
            host = request.get_host().split(':')[0]
            parts = host.split('.')
            # Example: store1.localhost → ['store1', 'localhost']
            if len(parts) > 2:
                domain = parts[0]

        # 3. Lookup vendor
        tenant = None
        if domain:
            try:
                tenant = Vendor.objects.get(domain=domain)
            except Vendor.DoesNotExist:
                return JsonResponse({"detail": "Invalid tenant domain"}, status=400)

        # 4. Attach tenant to request
        request.tenant = tenant

        return self.get_response(request)
