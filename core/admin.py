from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Authored

authored_inlines = ()
for subclass in Authored.__subclasses__():
    class SubclassInline(admin.TabularInline):
        model = subclass
        fk_name = 'author'
        extra = 0
    authored_inlines += (SubclassInline,)


@admin.register(User)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    inlines = authored_inlines
