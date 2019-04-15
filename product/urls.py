from django.conf.urls import url

from product.views import CreateProductView

urlpatterns = [
    url(r'^create/$', CreateProductView.as_view(), name='product_create'),
]