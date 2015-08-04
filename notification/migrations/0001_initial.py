# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('meta_status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='notifications_created', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(related_name='notification_recieved', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Notification',
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
