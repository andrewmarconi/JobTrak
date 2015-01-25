# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0004_auto_20150124_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='note',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companylocation',
            name='note',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
