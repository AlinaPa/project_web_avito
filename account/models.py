from django.contrib.auth.models import AbstractUser
from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    email = models.EmailField('Электронная почта', blank=False, unique=True)
    username = models.CharField('Имя пользователя', max_length=65,  blank=True, unique=True)

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
