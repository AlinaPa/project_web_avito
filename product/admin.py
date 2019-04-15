from django.contrib import admin
from django.contrib.admin import register
from product.models import Product


@register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', )

