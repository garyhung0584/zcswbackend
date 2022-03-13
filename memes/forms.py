from django import forms
from memes.models import Photo
#from memes.models import Comment


class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'description', 'image', 'tags', 'uploader')
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

'''
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
    }))
    
    class Meta:
        model = Comment
        fields = ('content')
'''