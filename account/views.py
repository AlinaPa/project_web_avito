from django.views.generic import FormView
from django import forms
from django.contrib.auth import authenticate, login

from account.models import User

from account.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login_form.html'
    success_url = "/"

    def get_template_names(self):
        return ['account/login_form.html'] if self.request.is_ajax() else [self.template_name]

    def form_valid(self, form):
        email_user = User.objects.filter(email__iexact=form.cleaned_data['email']).first()
        if email_user:
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(self.request, user)
            return super().form_valid(form)
        raise forms.ValidationError('Неверно указан email или пароль')
