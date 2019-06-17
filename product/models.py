from django.db import models


class ProductManage(models.Manager):
    def create_product(self, title):
        product = self.create(title=title)
        return product


class Product(models.Model):
    title = models.CharField('Название', max_length=100)
    # Todo: поправить price на DecimalField после того как доработаем парсер
    price = models.CharField('Цена', max_length=15, default=None)
    description = models.CharField('Описание', max_length=300)
    metro = models.CharField('Метро', max_length=300, blank=True)
    phone_number = models.CharField('Телефон', max_length=11)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    objects = ProductManage()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
