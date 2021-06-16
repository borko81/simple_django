from django import forms
from .models import BookModel, BookUserModel

"""
    • title – TextInput with class form-control
    • pages – NumberInput with class form-control
    • author – TextInput with class form-control
    • description – Textarea with class form-control
"""


class BookUserForm(forms.ModelForm):
    class Meta:
        model = BookUserModel
        fields = '__all__'


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
