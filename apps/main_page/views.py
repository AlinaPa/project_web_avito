from django.views.generic import ListView
from django.db.models import Q

from apps.news.models import News
from apps.product.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = "product_list"

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(Q(title__icontains=q))
        return queryset


class NewsListView(ListView):
    model = News
    template_name = 'main_page/header.html'
    paginate_by = 10
    context_object_name = 'news_list'

    def get_queryset(self):
        queryset = News.objects.all()
        return queryset
