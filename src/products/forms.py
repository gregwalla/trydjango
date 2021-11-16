from django import forms
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


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='', 
        widget = forms.TextInput(
                                attrs={
                                    "placeholder": "Your title"
                                })
                                )

    description = forms.CharField(
        required= False, 
        widget = forms.Textarea(attrs={
            "class" : "new class name",
            "id": "my-id-for-text-area",
            "rows" : 3        
                                    })
                                )

    price = forms.DecimalField()
