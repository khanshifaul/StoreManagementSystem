from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class CustomerForm(forms.Form):
    name = forms.CharField(label='',
                           max_length=128, required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    phone = forms.CharField(label='', max_length=11, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'required': True}))
    address = forms.CharField(label='', max_length=128, required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Address'}))


class ProductForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Product.objects.all(
    ), label='', required=False, empty_label='Select an Item')
    rate = forms.FloatField(label='', required=False, widget=forms.NumberInput(
        attrs={'placeholder': 'Rate'}))
    qty = forms.IntegerField(label='', required=False, initial=1, min_value=1, widget=forms.NumberInput(
        attrs={'placeholder': 'Quantity'}))
