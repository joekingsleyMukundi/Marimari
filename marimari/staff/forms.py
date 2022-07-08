from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CustomersForm(UserCreationForm):
    phone_number = forms.IntegerField()
    
    class Meta:
        model  = Customer
        fields = ['username', 'phone_number', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'phone_number':'Phone number',
            'password1': 'Password',
            'password2':'Confirm password',
        }