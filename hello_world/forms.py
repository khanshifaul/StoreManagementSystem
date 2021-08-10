from django import forms
from django.contrib.auth import models
from django.forms import Form, ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ManagerCreationForm(forms.Form):
    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class UserLoginForm():
    class Meta:
        model = User
        fields = ['username', 'password']
