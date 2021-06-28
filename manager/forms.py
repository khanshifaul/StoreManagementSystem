from django.forms import Form, ModelForm
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


class ProductForm(Form):
    class Meta:
        model = Product
        fields = 
