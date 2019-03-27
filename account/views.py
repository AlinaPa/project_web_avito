from _curses import flash

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login
from werkzeug.utils import redirect

from account.forms import LoginForm
from account.models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login_form.html'

    def get_template_names(self):
        return ['account/login_form.html'] if self.request.is_ajax() else [self.template_name]


def process_login():
    form = LoginForm
    if form.validate_on_submit():
        user = User.objects.filter(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login(user)
            flash("Вы вошлии на сайт")
            return redirect(url_for('index'))

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = LoginForm
#     return render(request, 'index.html', {'form': form})
