from django import forms
from django.forms.widgets import TextInput
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets ={
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'technology': TextInput(attrs={
                'class': 'form-control',
            })
        }
