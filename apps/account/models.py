from django.contrib.auth.models import AbstractUser
from django.db.models import Model, OneToOneField, DateField, Manager, CharField, CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from werkzeug.security import generate_password_hash, check_password_hash

from apps.utils.models import TimestampedModel


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


class RegistrationManager(Manager):
    def create_profile(self, user: User):
        return self.create(profile=user)


class Profile(TimestampedModel):
    user = OneToOneField(User, on_delete=CASCADE, verbose_name='Пользователь', related_name='profile')
    first_name = CharField('Имя', max_length=255, null=True, blank=True)
    last_name = CharField('Фамилия', max_length=255, null=True, blank=True)
    birthday = DateField('Дата рождения', null=True, default=None)

    department = CharField('Отдел', max_length=255, null=True, blank=True)
    position = CharField('Должность', max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', null=True, blank=True)
    telegram = CharField('Телеграм', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)

    objects = RegistrationManager()
