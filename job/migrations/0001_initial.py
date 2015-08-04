# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150804_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'Posted')),
                ('due', models.DateField(verbose_name=b'Due Date')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Job_Hirings',
                'verbose_name': 'Hiring',
                'verbose_name_plural': 'Hirings',
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Job Category')),
                ('description', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Job_Categories',
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Job_Types',
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
            },
        ),
        migrations.AddField(
            model_name='hiring',
            name='category',
            field=models.ForeignKey(related_name='category', to='job.JobCategory'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='company',
            field=models.ForeignKey(to='company.Company'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='job_type',
            field=models.ForeignKey(related_name='type', to='job.JobType'),
        ),
    ]
