from django.conf.urls import url, include
from django.contrib.admin import site

urlpatterns = [
    url(r'', include(('main_page.urls', 'main'))),
    url(r'^admin/', include((site.get_urls(), 'admin'))),
    url(r'^account/', include(('account.urls', 'account'))),
]
