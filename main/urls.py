from django.urls import path

from main.views import MainViews

urlpatterns = [
    path(r'', MainViews.as_view(), name='index'),
]