from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order/', OrderCreateView.as_view(), name='order-create'),
]
