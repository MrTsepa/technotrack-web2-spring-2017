from django.contrib import admin
from .models import Like
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

admin.site.register(Like)


class LikeInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Like
    ct_field = "target_content_type"
    ct_fk_field = "target_id"
    extra = 0
