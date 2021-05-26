from django import forms


class AskForm(forms.Form):
    name = forms.CharField(label='What you need', max_length=100)
