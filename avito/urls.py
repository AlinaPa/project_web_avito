from django.conf.urls import url, include
from django.contrib.admin import site

urlpatterns = [
    url(r'^admin/', include((site.get_urls(), 'admin'))),
    url(r'', include(('main.urls', 'main'))),
    url(r'^account/', include(('account.urls', 'account'))),
]
