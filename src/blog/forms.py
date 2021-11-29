from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='',  widget = forms.TextInput(  attrs={ "placeholder": "Your Article"}))
    description = forms.CharField(required= False, widget = forms.Textarea(attrs={
            "class" : "new class name",  "id": "my-id-for-text-area", "rows" : 3}))
    price = forms.DecimalField()

    class Meta:
        model = Article
        fields = [
            'title', 
            'description', 
            'price']

    def clean_title(self, *args, **kargs): 
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("CFE not in title")
        return title

