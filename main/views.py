from django.views.generic import ListView


class MainViews(ListView):
    template_name = 'main_page/header.html'

    def get_template_names(self):
        return ['main_page/header.html'] if self.request.is_ajax() else [self.template_name]