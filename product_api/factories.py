import factory
from factory import django
from django.conf import settings
from .models import Product, Order


class ProductFactory(django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("name")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    quantity_in_stock = factory.Faker("pyint", min_value=0, max_value=1000)


class OrderFactory(django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(settings.AUTH_USER_MODEL)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint", min_value=1, max_value=100)
