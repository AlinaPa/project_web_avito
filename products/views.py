from django.core.paginator import Paginator
from django.views.generic import ListView

from products.models import Products


class ProductListView(ListView):
    model = Products
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = "products"

    def get_queryset(self):
        return Products.objects.all()
