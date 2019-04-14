from django.db import models


class Products(models.Model):
    title = models.CharField('Название', max_length=100, default=None, blank=False)
    url = models.URLField('URL', blank=False)
    # Todo: поправить price на DecimalField после того как доработаем парсер
    price = models.CharField('Цена', max_length=15, default=None)
    description = models.CharField('Описание', max_length=300, blank=True)
    metro = models.CharField('Метро', max_length=300, blank=True)
    phone_number = models.CharField('Телефон', max_length=11, blank=False)
    created_at = models.DateField('Дата создания', blank=False)

    def __str__(self):
        return f'<Products: {self.title} {self.url}>'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
