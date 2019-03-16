import random
from django.db import models

random_number = str(random.randint(1000000000, 9999999999))


class Products(models.Model):
    number = models.CharField(verbose_name='Номер объявления', default=random_number, max_length=10)
    name = models.CharField(verbose_name='Название', max_length=100, blank=True)
    description = models.CharField(verbose_name='Описание', max_length=300, blank=True)
    created_at = models.DateField(verbose_name='Дата создания')
    price = models.DecimalField(verbose_name='Цена', default=None, null=True, max_digits=7, decimal_places=2)
    phone_number = models.CharField(verbose_name='Телефон', max_length=11, blank=True)

