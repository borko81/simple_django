from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = 'title description'.split()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(check in title for check in '@#$!%'):
            raise forms.ValidationError("Not alowed symbol in title")
        if title.lower() == title:
            title = title.title()
        return title
