from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash


class User(AbstractUser):
    username = models.CharField(_('Имя пользователя'), max_length=30, unique=True, blank=True)
    password = models.CharField(_('Пароль'), max_length=128, blank=True)
    email = models.EmailField(_('Электронная почта'), unique=True)

    def __str__(self):
        return self.username or self.email

    def __repr__(self):
        return self.email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser



