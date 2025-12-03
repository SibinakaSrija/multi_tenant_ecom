from django.urls import path
from .views import vendors_list_create, vendor_health

urlpatterns = [
    path('', vendors_list_create),
    path('health/', vendor_health),
]
