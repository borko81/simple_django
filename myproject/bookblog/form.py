from django import forms
from . models import Comment

class EmailForm(forms.Form):
    name = forms.CharField(max_length=32, label='Your name', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label="Your email", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    to = forms.EmailField(label='To email', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'name email body'.split()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})
        

        