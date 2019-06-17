from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username or self.email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='profile')
    birthday = models.DateField('Дата рождения', null=True, default=None)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)
