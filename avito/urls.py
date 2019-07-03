from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.admin import site

from avito import settings

urlpatterns = [
    url(r'', include(('main_page.urls', 'main_page'))),
    url(r'^admin/', include((site.get_urls(), 'admin'))),
    url(r'^account/', include(('account.urls', 'account'))),
    url(r'^product/', include(('product.urls', 'product'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
