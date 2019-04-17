from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView

from product.forms import CreateProductForm
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context


class CreateProductView(FormView):
    form_class = CreateProductForm
    template_name = 'products/create.html'
    success_url = "/product/success_create/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/view_product.html'
    context_object_name = "product"

    def product_detail_view(request, pk):
        product_id = get_object_or_404(Product, pk=pk)
        return render(request, 'products/view_product.html', context={'product': product_id,})
