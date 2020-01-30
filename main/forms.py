from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from main.models import Task, Store, DeliveryBoy


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class StoreForm(forms.ModelForm):
    validation_messages = {
        "duplicate_store": "seller name already exists",
        "duplicate_number": "number already exists with in gobd.delivery"
    }

    class Meta:
        model = Store
        fields = ('store_name', 'contact_number', 'business_name', 'division',
                  'district', 'upazila', 'business_address', 'nid_number', 'verification')

        labels = {
            'store_name': "seller name",
            'contact_number': "in +8801XXXXXXXXX pattern",
            'business_name': "business name",
            'division': "division",
            'district': "district",
            'upazila': "upazila",
            'business_address': "business address",
            'nid_number': "a valid identification number",
            'verification': "upload verification image",
        }

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['store_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['business_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['division'].widget.attrs.update({'class': 'form-control'})
        self.fields['district'].widget.attrs.update({'class': 'form-control'})
        self.fields['upazila'].widget.attrs.update({'class': 'form-control'})
        self.fields['business_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['nid_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['verification'].widget.attrs.update({'class': 'form-control'})

    def clean_store_name(self):
        sn_instance = self.cleaned_data.get("store_name")
        validate = self.__class__._meta.model._default_manager.filter(store_name=sn_instance).exists()
        if validate:
            raise ValidationError(self.validation_messages.get("duplicate_store"))

    def clean_contact_number(self):
        cn_instance = self.cleaned_data.get("contact_number")
        validate = self.__class__._meta.model._default_manager.filter(contact_number=cn_instance).exists()
        if validate:
            raise ValidationError(self.validation_messages.get("dupicate_number"))


# class DeliveryBoyForm(forms.ModelForm):
#     validation_messages = {
#         "duplicate_number": "number already exists with gobd.delivery"
#     }
#
#     class Meta:
#         model = DeliveryBoy
#         fields = ('name', 'number', 'email', 'division',
#                   'district', 'upazila', 'address', 'nid_number', 'verification')
#
#         labels = {
#             'name': "delivery boy name",
#             'number': "in +8801XXXXXXXXX pattern",
#             'email': "your e mail id",
#             'division': "division",
#             'district': "district",
#             'upazila': "upazila",
#             'address': "business address",
#             'nid_number': "a valid identification number",
#             'verification': "upload verification image",
#         }
#
#         def __init__(self, *args, **kwargs):
# 			super(DeliveryBoyForm, self).__init__(*args, **kwargs)
# 			self.fields['name'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['number'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['email'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['division'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['district'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['upazila'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['address'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['nid_number'].widget.attrs.update({'class': 'form-control'})
# 			self.fields['verification'].widget.attrs.update({'class': 'form-control'})
#
#     def clean_contact_number(self):
#         cn_instance = self.cleaned_data.get("number")
#         validate = self.__class__._meta.model._default_manager.filter(number=cn_instance).exists()
#         if validate:
#             raise ValidationError(self.validation_messages.get("dupicate_number"))

class DeliveryBoyForm(forms.ModelForm):

	validation_messages = {
		"dupicate_number": "Number Already exists with Store"
	}

	class Meta:
		model = DeliveryBoy
		fields = ('number',)

		labels = {
			'number': "Enter Contact Number"
		}

	def clean_contact_number(self):
		cn_instance = self.cleaned_data.get("number")
		validate = self.__class__._meta.model._default_manager.filter(number=cn_instance).exists()
		if validate:
			raise ValidationError(self.validation_messages.get("dupicate_number"))


class TaskForm(forms.ModelForm):
    validation_messages = {
        "Title_Error": "please enter the product title in a different way"
    }

    class Meta:
        model = Task
        fields = ('title', 'priority', 'status', 'weight', 'customer_name', 'customer_contact_no',
                  'division', 'district', 'upazila', 'delivery_location', 'delivery_note', 'product_price',
                  'payment_type')

        labels = {
            "title": "product name",
            "priority": "select priority",
            "status": "oder status",
            "weight": "product weight",
            "customer_name": "customer name",
            "customer_contact_no": "customer contact number in 01XXXXXXXXX format",
            "division": "division",
            "district": "district",
            "upazila": "upazila",
            "delivery_location": "product delivery location",
            "delivery_note": "Any Additional Notes During The Delivery",
            "product_price": "Price of Your Product",
            "payment_type": "Select Payment Type"

        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control'})
        self.fields['customer_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['customer_contact_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['division'].widget.attrs.update({'class': 'form-control'})
        self.fields['district'].widget.attrs.update({'class': 'form-control'})
        self.fields['upazila'].widget.attrs.update({'class': 'form-control'})
        self.fields['delivery_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['delivery_note'].widget.attrs.update({'class': 'form-control'})
        self.fields['product_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_type'].widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        title_instance = self.cleaned_data.get("title")
        validate = Task.objects.filter(title=title_instance, status=Task.PICKUP).exists()
        if validate:
            raise ValidationError(validation_messages["Title_Error"])
        return title_instance
