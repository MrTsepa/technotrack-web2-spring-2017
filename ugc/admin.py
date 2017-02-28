from django.contrib import admin

from likes.admin import LikeInline
from ugc.models import Post


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = LikeInline,
