from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

