from django.conf.urls import url

from account.views import LoginView, RegisterView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
]