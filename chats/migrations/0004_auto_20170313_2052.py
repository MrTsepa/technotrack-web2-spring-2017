# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20170313_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.Chat'),
        ),
    ]
