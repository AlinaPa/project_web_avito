from django.contrib import admin
from django.contrib.admin import register

from profile.models import Profile, User


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'view', )


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )
