import uuid

from django.db import models
from django.conf import settings

# There some extensions that can do it, but I didn't want to introduce too many dependencies
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# TODO refactor into separate modules
class Product(UUIDModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name
    

class Order(UUIDModel):
    PENDING = "P"
    COMPLETED = "C"
    STATUS_CHOICES = ((PENDING, "pending"), (COMPLETED, "completed"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    
# TODO if I had more time I'd add OrderItem, ProductCategory, Address, Invoice, Billing
    # shipping_address = models.ForeignKey(
    #     Address,
    #     related_name="shipping_orders",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )
    # billing_address = models.ForeignKey(
    #     Address,
    #     related_name="billing_orders",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )
