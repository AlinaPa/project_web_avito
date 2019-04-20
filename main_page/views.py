from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = "product_list"
