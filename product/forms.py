from django import forms

from product.models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'metro',
            'phone_number',
            'photo',
        )
