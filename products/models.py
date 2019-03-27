from django.db import models
from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    title = models.CharField(_('Название'), max_length=100, default=None, blank=False)
    url = models.URLField(_('URL'), blank=False)
    # Todo: поправить price на DecimalField после того как доработаем парсер
    price = models.CharField(_('Цена'), max_length=15, default=None)
    description = models.CharField(_('Описание'), max_length=300, blank=True)
    metro = models.CharField(_('Метро'), max_length=300, blank=True)
    phone_number = models.CharField(_('Телефон'), max_length=11, blank=False)
    created_at = models.DateField(_('Дата создания'), blank=False)

    def __repr__(self):
        return f'<Products: {self.title} {self.url}>'


