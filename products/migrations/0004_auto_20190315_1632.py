# Generated by Django 2.1.7 on 2019-03-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190315_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='number',
            field=models.CharField(default='9496648623', max_length=10, verbose_name='Номер объявления'),
        ),
        migrations.AlterField(
            model_name='products',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, verbose_name='Телефон'),
        ),
    ]