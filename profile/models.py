from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_fsm import FSMField
from model_utils import Choices


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


class Profile(models.Model):
    VIEW = Choices(
        ('PRIVATE_PERSON', 'Частное лицо'),
        ('LEGAL_PERSON', 'Юридическое лицо'),
        ('REALTOR', 'Риэлтор'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    view = FSMField(_('Вид профиля'), choices=VIEW, protected=True)


