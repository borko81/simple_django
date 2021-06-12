from django import forms
from django.core.exceptions import ValidationError


def check_name_length(value):
    if not value[0] == value[0].upper():
        raise ValidationError('Name must be start with uppercase')
    if not len(value) > 3:
        raise ValidationError('Name must be big from three symbol')


def validate_age_is_bigger_from_zero(value):
    if value <= 17:
        raise ValidationError('Age must be bigger from 18')

class MyForm(forms.Form):
    name = forms.CharField(
        validators=[check_name_length],
        widget=forms.TextInput()
    )
    age = forms.IntegerField(
        validators=[validate_age_is_bigger_from_zero],
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    text = forms.CharField(
        widget=forms.Textarea()
    )

