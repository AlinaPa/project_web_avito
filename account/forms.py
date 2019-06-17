from django import forms
from django.contrib.auth.forms import UsernameField, UserCreationForm

from account.models import User


class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

