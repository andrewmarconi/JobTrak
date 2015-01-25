# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0016_joblisting_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionhistory',
            name='when',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
            preserve_default=True,
        ),
    ]
