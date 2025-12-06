from django.urls import path
from .views import product_list_create, product_detail
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='products')


urlpatterns = [
    path('products/', product_list_create),
    path('products/<int:pk>/', product_detail),
    path('', include(router.urls)),
]

