import uuid
from django.db import models
from accounts.models import *


# Create your models here.

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    customer = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.CharField(max_length=5, null=True, blank=True)
    amount = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.customer)
