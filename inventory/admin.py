from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (
    Supplier, Brand,
    Category, Device,
    DeviceMeta, Order,
    OrderItems, OrderNotes,
    Profile)



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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Order, OrderAdmin)
