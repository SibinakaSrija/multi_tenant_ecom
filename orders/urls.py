from django.urls import path
from .views import create_order, list_orders
from django.urls import path
from .views import place_order

urlpatterns = [
    path('orders/', list_orders),
    path('orders/create/', create_order),
    path('place/', place_order),
    path('', list_orders),
]



