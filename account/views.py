from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import FormView, TemplateView
from django import forms
from django.contrib.auth import authenticate, login, logout

from account.forms import LoginForm, RegistrationForm
from account.models import User, Profile


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login_form.html'
    success_url = "/"

    def form_valid(self, form):
        username = User.objects.filter(username__iexact=form.cleaned_data['username']).first()
        if username:
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(self.request, user)
            return super().form_valid(form)
        raise forms.ValidationError('Неверно указан email или пароль')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "account/registration_form.html"
    success_url = "/account/login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    model = Profile
    template_name = "account/profile.html"

