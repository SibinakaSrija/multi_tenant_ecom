from django.urls import path
from .views import vendors_list_create, vendor_detail, vendor_health

urlpatterns = [
    path('vendors/', vendors_list_create),
    path('vendors/<int:pk>/', vendor_detail),
    path('vendors/health/', vendor_health),
]
