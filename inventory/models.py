from django.db import models
from .utils import  max_value_current_year
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


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
    class OrderStatus(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        DEPLOYED = 'DEPLOYED', 'Deployed'
        RECEIVED = 'RECEIVED', 'Received'
        RETURN = 'RETURNED', 'Returned'

    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issued_to")
    issued_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="issued_by")
    issued_on = models.DateField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.DRAFT)


    def __str__(self):
        return f'{self.issued_to.username} Order -- {self.item_count} item(s)'

    @property
    def item_count(self):
        return self.orderitems_set.all().count()


class OrderItems(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)
    serial_number = models.CharField(max_length=200, default='', blank=True)
    product_number = models.CharField(max_length=200, default='', blank=True)
    device_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f'{self.order.id} - {self.device.name}'

    class Meta:
        verbose_name_plural = "Order Items"


class OrderNotes(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='created_by')
    notes = models.TextField(null=True, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Order Notes"


class Profile(models.Model):
    class Department(models.TextChoices):
        PBB = 'PBB', 'PBB'
        ADMIN_HR = 'ADMIN_HR', 'Admin/HR'
        FINANCE = 'FINANCE', 'Finance'
        ELP = 'ELP', 'ELP'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    department = models.CharField(max_length=30, choices=Department.choices, default=Department.PBB)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


