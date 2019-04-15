from django.views.generic import ListView, FormView

from product.forms import CreateProductForm
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.all()


class CreateProductView(FormView):
    form_class = CreateProductForm
    template_name = 'products/create.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
