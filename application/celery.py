from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')


app = Celery('application')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        schedule=crontab(hour=10, minute=0),
        task=daily_mailing
    )


@app.task
def daily_mailing():
    from mailing.models import MailingList
    user_ids = MailingList.objects.get(name='daily_mailing').users.values_list('id', flat=True)
    send_mail.chunks(user_ids, 5).apply_async()


@app.task
def send_mail(user_id):
    user = get_user_model().objects.get(id=user_id)
    from mailing.utils import send_daily_template_mail
    import datetime
    send_daily_template_mail(user, datetime.datetime.now().date())
