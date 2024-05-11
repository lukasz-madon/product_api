from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Product, Order
from .serializers import OrderSerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            product_id = request.data.get('product_id')
            quantity = int(request.data.get('quantity'))
            
            product = Product.objects.select_for_update().get(id=product_id)
            if product.quantity_in_stock >= quantity:
                product.quantity_in_stock -= quantity
                product.save()

                order = Order.objects.create(
                    user=request.user,
                    product=product,
                    quantity=quantity
                )
                # raise serializers.ValidationError(error) 
                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
