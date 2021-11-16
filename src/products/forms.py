from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price'
        ]


class RawProductForm(forms.FORM):
    title = forms.Charfield()
    description = forms.Charfield()
    price = forms.DecimalField()
