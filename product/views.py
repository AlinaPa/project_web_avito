from django.views.generic import ListView, DetailView, CreateView

from product.models import Product


class CreateProductView(CreateView):
    model = Product
    fields = (
        'title',
        'description',
        'price',
        'metro',
        'phone_number',
    )
    template_name = 'products/create.html'
    success_url = "/product/success_create/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/view_product.html'
