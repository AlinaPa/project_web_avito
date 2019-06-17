from django.conf.urls import url

from account.views import LoginView, RegisterView, ProfileView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]
