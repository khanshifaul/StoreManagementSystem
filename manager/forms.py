from django.forms import ModelForm, widgets
from .models import *
from django.utils.translation import gettext_lazy as _


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'address')
        labels = {
            'name': _('Name'),
            'phone': _('Phone'),
            'address': _('Address'),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
