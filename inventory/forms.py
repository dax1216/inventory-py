from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Supplier, Brand, Category, Device, DeviceMeta


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceMetaForm(ModelForm):
    class Meta:
        model = DeviceMeta
        fields = '__all__'

DeviceMetaFormSet = inlineformset_factory(
    Device, DeviceMeta, form=DeviceForm,
    extra=1, can_delete=True, can_delete_extra=True
)
