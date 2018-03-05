from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfile_Info

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model =User
        fields =('username','email','password')


class User_Profile_Info(forms.ModelForm):
    class Meta():
        model = UserProfile_Info
        fields= ('profile_site','profile_pic')
