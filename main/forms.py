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
<<<<<<< HEAD
    ''' 
=======

>>>>>>> 021a895 (希望這樣是對的)
    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
<<<<<<< HEAD
        return user'''
        
class UserEditForm(forms.ModelForm):
=======
        return user

class UserEditForm(ModelForm):
>>>>>>> 021a895 (希望這樣是對的)
    
    class Meta:
        model = Member
        fields = '__all__'
<<<<<<< HEAD
        exclude = ['user', 'imguploaded', 'likes']
=======
        exclude = ['user', "imguploaded", "likes"]
>>>>>>> 021a895 (希望這樣是對的)
