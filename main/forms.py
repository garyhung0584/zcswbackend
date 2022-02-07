from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Member

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ("intro", "profile_pic")
        
    def save(self, commit = True):
        member = super(UserEditForm, self).save(commit = False)
        member.intro = self.cleaned_data['intro']
        if commit:
            member.save()
        return member