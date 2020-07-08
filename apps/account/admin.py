from django.contrib import admin
from django.contrib.admin import register

from apps.account.models import User, Profile


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff')


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', )
