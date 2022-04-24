from django import forms
from memes.models import Photo, Tag
#from memes.models import Comment

class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'description', 'image', 'tags', 'uploader')
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'hey'})
'''
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
    }))
    
    class Meta:
        model = Comment
        fields = ('content')
'''
