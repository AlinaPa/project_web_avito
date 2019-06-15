from django.conf.urls import url, include
from django.contrib.admin import site

urlpatterns = [
    url(r'^admin/', include((site.get_urls(), 'admin'))),
    url(r'^account/', include(('account.urls', 'account'))),
    url(r'^product/', include(('product.urls', 'product'))),
    url(r'', include(('main_page.urls', 'main_page'))),
]
