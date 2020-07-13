from django.db.models import Model, Manager, CharField, ImageField, DateTimeField


class ProductManage(Manager):
    def create_product(self, title):
        return self.create(title=title)


class Product(Model):
    title = CharField(verbose_name='Название', max_length=100)
    # Todo: поправить price на DecimalField после того как доработаем парсер
    price = CharField(verbose_name='Цена', max_length=15, default=None)
    description = CharField(verbose_name='Описание', max_length=300)
    metro = CharField(verbose_name='Метро', max_length=300, blank=True)
    phone_number = CharField(verbose_name='Телефон', max_length=11)
    photo = ImageField(verbose_name='Фотография', null=True, default=None, upload_to='products')
    created_at = DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    objects = ProductManage()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
