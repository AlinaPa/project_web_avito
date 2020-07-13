from django.conf.urls import url

from apps.main_page.views import NewsListView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='index'),
]
