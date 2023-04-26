from django.db import models


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
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Device(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
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

