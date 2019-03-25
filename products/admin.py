from django.contrib import admin
from django.contrib.admin import register
from products.models import Products


@register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', )

