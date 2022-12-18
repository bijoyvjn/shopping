from django.forms import ModelForm
from .models import *
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
