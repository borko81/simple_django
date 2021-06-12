from django import forms


class MyForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput()
    )
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    text = forms.CharField(
        widget=forms.Textarea()
    )