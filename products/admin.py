from django.contrib import admin
from django.contrib.admin import register
from products.models import Products


@register(Products)
class ProdactsAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'price', 'phone_number', )
