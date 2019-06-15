from django.views.generic import ListView
from django.db.models import Q
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = "product_list"

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(Q(title__icontains=q))
        return queryset
