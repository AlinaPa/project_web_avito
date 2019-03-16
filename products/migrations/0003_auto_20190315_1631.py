# Generated by Django 2.1.7 on 2019-03-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190315_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='comment',
        ),
        migrations.AddField(
            model_name='products',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='products',
            name='number',
            field=models.CharField(default='5619359172', max_length=10, verbose_name='Номер объявления'),
        ),
    ]
