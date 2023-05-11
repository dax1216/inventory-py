from django.forms import ModelForm
from django.forms import inlineformset_factory, modelformset_factory
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


DeviceMetaFormSet = modelformset_factory(DeviceMeta, fields=["meta_key", "meta_value"], can_delete=True)
