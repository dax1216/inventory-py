from django.contrib import admin
from .models import Supplier, Brand, Category, Device, DeviceMeta

class DeviceMetaInline(admin.StackedInline):
    model = DeviceMeta
    extra = 1


class DeviceAdmin(admin.ModelAdmin):
    inlines = [DeviceMetaInline]


# Register your models here.
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceMeta)
