from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.admin import site

from avito import settings

urlpatterns = [
    url(r'^account/', include(('apps.account.urls', 'account'))),
    url(r'^admin/', include((site.get_urls(), 'admin'))),
    url(r'^product/', include(('apps.product.urls', 'product'))),
    url(r'', include(('apps.main_page.urls', 'main_page'))),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL,
                                                                                  document_root=settings.MEDIA_ROOT)

