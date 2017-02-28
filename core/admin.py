from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ugc.admin import PostInline
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    inlines = PostInline,
