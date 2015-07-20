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
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.ImageField(upload_to=b'images/companythumbs/')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('address', models.CharField(max_length=255, verbose_name=b'Address')),
                ('country', models.CharField(max_length=100, verbose_name=b'Country')),
                ('province', models.CharField(max_length=100, verbose_name=b'Province')),
                ('postal_code', models.SmallIntegerField(default=6000, verbose_name=b'Postal Code')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('website', models.URLField(verbose_name=b'Website', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Company',
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False, verbose_name=b'Status')),
                ('company', models.OneToOneField(to='company.Company')),
            ],
            options={
                'db_table': 'Company_Status',
                'verbose_name': 'Company Status',
                'verbose_name_plural': 'Company Status',
            },
        ),
    ]
