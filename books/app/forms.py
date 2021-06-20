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

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].isdigit():
            self.add_error('name', 'Must not be start with digit!')

        return name


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title[0].isupper():
            self.add_error('title', 'Should start with upper case!')

        if title.endswith('.'):
            self.add_error('title', 'Should not be end with dot!')

        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if description[0].isdigit():
            self.add_error('description', 'Must not be start with digit!')

        return description