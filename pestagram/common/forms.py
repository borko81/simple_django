from django import forms

from common.models import Pet, Comment


class CreatePetForm(forms.ModelForm):
    type = forms.ChoiceField(choices=[("DOG", "dog"), ("CAT", "cat"), ("PARROT", "parrot")], required=True,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 },

                             ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    age = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Pet
        fields = ('type', 'name', 'age', 'description', 'image_url')


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

