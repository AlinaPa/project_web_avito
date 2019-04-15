from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта пользователя', max_length=150)
    password = forms.CharField(label='Пароль', max_length=8, widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2'
        )
