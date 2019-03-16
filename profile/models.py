from django.db import models
from django_fsm import FSMField
from model_utils import Choices


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=True)
    created_at = models.DateField()


class Profile(models.Model):
    VIEW = Choices(
        ('PRIVATE_PERSON', 'Частное лицо'),
        ('LEGAL_PERSON', 'Юридическое лицо'),
        ('REALTOR', 'Риэлтор'),
    )
    user = models.OneToOneField(User, models.PROTECT, verbose_name='Пользователь', related_name='profile')
    view = FSMField(verbose_name='Вид профиля', choices=VIEW, protected=True)


