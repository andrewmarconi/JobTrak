# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0015_joblisting_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='date_posted',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
