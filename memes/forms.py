from django import forms
from memes.models import Photo, Tag, Comment, Report
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

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
    }))
    
    class Meta:
        model = Comment
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ("__all__")
