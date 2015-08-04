# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150801_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystatus',
            name='company',
            field=models.OneToOneField(related_name='status', to='company.Company'),
        ),
    ]
