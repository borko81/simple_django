from django.forms import models
from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
