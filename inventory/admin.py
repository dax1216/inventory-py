from django.contrib import admin
from .models import (
    Supplier, Brand,
    Category, Device,
    DeviceMeta, Order,
    OrderItems, OrderNotes)


class DeviceMetaInline(admin.StackedInline):
    model = DeviceMeta
    extra = 1


class DeviceAdmin(admin.ModelAdmin):
    inlines = [DeviceMetaInline]


class OrderItemsInline(admin.StackedInline):
    model = OrderItems
    extra = 1


class OrderNotesInline(admin.StackedInline):
    model = OrderNotes
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline, OrderNotesInline]
    readonly_fields = ('issued_by',)


# Register your models here.
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Order, OrderAdmin)
