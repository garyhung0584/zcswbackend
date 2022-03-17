from django import forms
from memes.models import Photo, Tag

class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'description', 'image', 'tags', 'uploader')
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
