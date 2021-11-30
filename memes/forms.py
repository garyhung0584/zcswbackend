from django import forms
from memes.models import Photo


class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'id': 'upload_pic'})
        }