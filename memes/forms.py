from django import forms
<<<<<<< Updated upstream
from memes.models import Photo
=======
from memes.models import Photo, Tag ,Report
#from memes.models import Comment
>>>>>>> Stashed changes


class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Photo
<<<<<<< Updated upstream
        fields = ('title', 'description', 'image',)
=======
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

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ("__all__")
>>>>>>> Stashed changes
