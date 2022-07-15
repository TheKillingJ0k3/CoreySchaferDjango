from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta: #gies us nested namespace for configurations, affected model = user, we specify fields
        model = User
        fields = ['username', 'email', 'password1', 'password2']
