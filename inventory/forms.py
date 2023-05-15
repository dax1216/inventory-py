from django.forms import ModelForm, modelformset_factory
from django import forms
from .utils import year_choices, current_year
from .models import (
    Supplier, Brand,
    Category, Device,
    DeviceMeta, Order, OrderItems)


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
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

    class Meta:
        model = Device
        fields = '__all__'


class DeviceMetaForm(ModelForm):
    class Meta:
        model = DeviceMeta
        fields = '__all__'


DeviceMetaFormSet = modelformset_factory(DeviceMeta, fields=["meta_key", "meta_value"], can_delete=True)


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['issued_to', 'issued_on']

        widgets = {
            'issued_on': DatePickerInput(),
        }



class OrderItemsForm(ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'



OrderItemsFormSet = modelformset_factory(OrderItems,
                                         fields=["device", "serial_number", "product_number"],
                                         can_delete=True)
