from django.db import transaction
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, serializers, status, views, viewsets
from rest_framework.response import Response

from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer


# TODO finish docs
@extend_schema(
    summary="List all products",
    parameters=[]
)
class ProductViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **products** in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: http://example.com/TODO
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **orders** for the given user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        This view returns a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.select_related("product").filter(user=user)


    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity"))

        order, error = create_order(request.user, product_id, quantity)
        if not order:
            raise serializers.ValidationError(error)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


# TODO move to a business layer
def create_order(user, product_id, quantity):
    """
    creates a new order in a single atomic transaction

    avoid race condiation using select_for_update
    """
    with transaction.atomic():
        product = get_object_or_404(Product.objects.select_for_update(), id=product_id)
        if product.quantity_in_stock >= quantity:
            product.quantity_in_stock -= quantity
            product.save()

            order = Order.objects.create(user=user, product=product, quantity=quantity)
            return order, None
        else:
            return None, "Not enough stock available"
