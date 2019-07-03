from django.views.generic import DetailView, CreateView

from product.forms import CreateProductForm
from product.models import Product


class CreateProductView(CreateView):
    form_class = CreateProductForm
    template_name = 'products/create.html'
    success_url = "/product/success_create/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/view_product.html'
