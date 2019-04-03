from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта пользователя', max_length=150)
    password = forms.CharField(label='Пароль', max_length=6, widget=forms.PasswordInput)
