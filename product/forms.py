from django import forms

from product.models import Product


class CreateProductForm(forms.Form):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'description',
            'metro',
            'phone_number',
        )
