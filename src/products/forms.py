from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',  widget = forms.TextInput(  attrs={ "placeholder": "Your title"}))
    description = forms.CharField(required= False, widget = forms.Textarea(attrs={
            "class" : "new class name",  "id": "my-id-for-text-area", "rows" : 3}))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price']

    def clean_title(self, *args, **kargs): 
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("CFE not in title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='',  widget = forms.TextInput(  attrs={ "placeholder": "Your title"}))
    description = forms.CharField(required= False, widget = forms.Textarea(attrs={
            "class" : "new class name", "id": "my-id-for-text-area", "rows" : 3}))
    price = forms.DecimalField()
