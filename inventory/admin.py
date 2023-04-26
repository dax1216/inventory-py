from django.contrib import admin
from .models import Supplier, Brand, Category, Device
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Device)
