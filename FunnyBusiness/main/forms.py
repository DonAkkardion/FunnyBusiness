from dataclasses import field
from .models import Products
from django.forms import ModelForm, CheckboxInput, ClearableFileInput
from django.forms import TextInput, NumberInput, RadioSelect
from django.forms import Textarea, Select




class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description","price","isAvailable","category","img"]
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter Product Name'
            }),
            "description": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Enter Product Description'
            }),
            "price": NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter Product Price'
            }),
            "category": Select(attrs={                    
                'class':'form-control',
                'placeholder': ''
            }),
            "img": ClearableFileInput(attrs={                    
                'class':'form-control',
                'placeholder': 'Enter'
            }),
            
            

        }