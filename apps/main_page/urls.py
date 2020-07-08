from django.conf.urls import url

from apps.main_page.views import ProductListView

urlpatterns = [
    url(r'', ProductListView.as_view(), name='index'),
]
