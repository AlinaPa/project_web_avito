from django.views.generic import ListView

from products.models import Products


class ProductListView(ListView):
    model = Products
    template_name = 'main_page/header.html'