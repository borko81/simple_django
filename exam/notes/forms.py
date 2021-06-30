from django import forms

from notes.models import Profile, Note


class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteForms(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']


class NoteFormsDisabled(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteFormsDisabled, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['disabled'] = True
        self.fields['content'].widget.attrs['disabled'] = True
        self.fields['image_url'].widget.attrs['disabled'] = True

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']
