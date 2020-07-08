from django.conf.urls import url
from django.views.generic import TemplateView

from apps.product.views import ProductDetailView, CreateProductView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='view_product'),
    url(r'^create/$', CreateProductView.as_view(), name='product_create'),
    url(r'^success_create/$', TemplateView.as_view(template_name='products/success_create.html'),
        name='success_create'),
]
