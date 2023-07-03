from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields =  ('Name','cal','username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
         model = CustomUser
         fields =  ('Name','cal','username', 'email')
