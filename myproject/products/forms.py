from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title description price'.split()


class RawProductForm(forms.Form):
    title = forms.CharField(label="New Title", widget=forms.TextInput(attrs={
        "placeholder": "Enter title here"
    }))
    description = forms.CharField(label="New Description", widget=forms.Textarea(attrs={
        "placeholder": "Description",
        "class": "new-class-name",
        "rows": 10,
        "cols": 30,
    }))
    price = forms.DecimalField(label="New price", initial=0.99)
