from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Member

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    ''' 
    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user'''
        
class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ('profile_pic','username','intro')
        #exclude = ['user', 'imguploaded', 'likes']
        
        
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs.update({
            'onchange' : 'display_image(event)'
        })
