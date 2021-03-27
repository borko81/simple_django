from django import forms

from .models import Product

NOT_ALLOWED_SYMOBOL = '@!^[]-'


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="New Title", widget=forms.TextInput(attrs={
        "placeholder": "Enter name of the product"
    }))

    class Meta:
        model = Product
        fields = 'title description price'.split()

    def clean_title(self):
        """ Validate title check if any symbol is not alowed """
        title = self.cleaned_data.get('title')
        if any(i in title for i in NOT_ALLOWED_SYMOBOL):
            raise forms.ValidationError(f"{title} not allowed by name")
        return title.title()


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
