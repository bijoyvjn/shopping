from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'pin',
                  'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Phone number',
                                            'pattern': '[0-9]{6,11}',
                                            'title': 'Phone number should be 6 to 11 digits'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Address'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'City'}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'State'}),
            'pin': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Pin'}),
            'password1': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Password'}),
            'password2': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Confirm Password'}),
        }
