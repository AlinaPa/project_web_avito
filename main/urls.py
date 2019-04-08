from django.urls import path

from main.views import ProductListView

urlpatterns = [
    path(r'', ProductListView.as_view(), name='index'),
]