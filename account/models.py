from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('Профиль'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("Пользователь с таким именем уже существует."),
        },
        blank=True
    )

    first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30, blank=True)
    password = models.CharField(_('Пароль'), max_length=128, blank=True)
    email = models.EmailField(_('Электронная почта'), unique=True, blank=True)

    class Meta(AbstractUser.Meta):
        pass




