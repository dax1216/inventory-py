from django.forms import ModelForm, modelformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from .utils import year_choices, current_year
from .models import (
    Supplier, Brand,
    Category, Device,
    DeviceMeta, Order,
    OrderItems, Profile)


DEPARTMENTS = (
        ('PBB', 'PBB'),
        ('ADMIN_HR', 'Admin/HR'),
        ('FINANCE', 'Finance'),
        ('ELP', 'ELP')
    )


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
        fields = ['issued_to', 'issued_on', 'status']

        widgets = {
            'issued_on': DatePickerInput(),
        }



class OrderItemsForm(ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'



OrderItemsFormSet = modelformset_factory(OrderItems,
                                         fields=["device", "serial_number", "product_number","device_image"],
                                         can_delete=True)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UpdateUserForm(forms.ModelForm):
    # username = forms.CharField(max_length=100,
    #                            required=True,
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True,
    #                          widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):

    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    department = forms.ChoiceField(choices=DEPARTMENTS)
    class Meta:
        model = Profile
        fields = ['avatar', 'department']


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

