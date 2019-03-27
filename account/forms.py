from django import forms
from django.contrib.auth import authenticate, login

from account.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта пользователя', max_length=150)
    password = forms.CharField(label='Пароль', max_length=6, widget=forms.PasswordInput)
    user = None

    def clean_email(self):
        if not User.objects.filter(email__iexact=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Пользователя с таким email не найдено')
        return self.cleaned_data['email']

    def clean(self):
        if self._errors:
            return

    def process_login(self, request):
        email_user = User.objects.filter(email__iexact=self.data['email']).first()
        user = authenticate(username=email_user.username, password=self.data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                raise forms.ValidationError('Такого пользователя не существует')
        else:
            raise forms.ValidationError('Неверно указан email или пароль')

