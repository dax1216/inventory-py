from django.db import models
from django.conf import settings
from .utils import  max_value_current_year
from django.core.validators import MaxValueValidator, MinValueValidator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_num = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='parent_cat', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Device(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(null=True, validators=[MinValueValidator(2010), max_value_current_year])
    quantity = models.IntegerField(default=0)
    defective = models.IntegerField(default=0)
    returned = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DeviceMeta(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    meta_key = models.CharField(null=False, blank=False, max_length=255)
    meta_value = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.meta_key;


class Order(models.Model):
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issued_to")
    issued_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="issued_by")
    issued_on = models.DateField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)
    serial_number = models.CharField(max_length=200, default='', blank=True)
    product_number = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return f'{self.order.id} - {self.device.name}'

    class Meta:
        verbose_name_plural = "Order Items"


class OrderNotes(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(null=True, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order Notes"



