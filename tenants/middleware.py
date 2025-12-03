from tenants.models import Vendor

class TenantMiddleware:
    """
    Extract tenant from X-Tenant-Domain header or subdomain and attach request.tenant.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        domain = request.META.get('HTTP_X_TENANT_DOMAIN')
        if not domain:
            host = request.get_host().split(':')[0]
            parts = host.split('.')
            if len(parts) > 2:
                domain = parts[0]
        tenant = None
        if domain:
            try:
                tenant = Vendor.objects.get(domain=domain)
            except Vendor.DoesNotExist:
                tenant = None
        request.tenant = tenant
        return self.get_response(request)
