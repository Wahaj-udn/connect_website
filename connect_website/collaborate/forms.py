# C:\Users\Admin\connect_website\collaborate\forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Idea, UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'interests', 'profile_picture']
