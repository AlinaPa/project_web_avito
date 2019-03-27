from django import forms
from django.contrib.auth import authenticate, login
from django.middleware.csrf import rotate_token

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

        email_user = User.objects.filter(email__iexact=self.data['email']).first()
        user = authenticate(username=email_user.username, password=self.data['password'])
        if user is not None:
            if user.is_active:
                self.user = user
            else:
                raise forms.ValidationError('На вашу электронную почту отправлено письмо '
                                            'с ссылкой на активацию аккаунта')
        else:
            raise forms.ValidationError('Неверно указан email или пароль')

    def login(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                raise forms.ValidationError('Такого пользователя не существует')
        else:
            raise forms.ValidationError('Неверно указан email или пароль')

