from django.urls import path

from main_page.views import ProductListView

urlpatterns = [
    path(r'', ProductListView.as_view(), name='index'),
]
