from django.contrib import admin

# Register your models here.
from mailing.models import MailingList

admin.site.register(MailingList)
