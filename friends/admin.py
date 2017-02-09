from django.contrib import admin

from friends.models import Friendship, Friend

admin.site.register(Friendship)
admin.site.register(Friend)
