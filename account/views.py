from django.views.generic import FormView

from account.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    # success_url = '/'
    template_name = 'account/login_form.html'

    def get_template_names(self):
        return ['account/login_form.html'] if self.request.is_ajax() else [self.template_name]
