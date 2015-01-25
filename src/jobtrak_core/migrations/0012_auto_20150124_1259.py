# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0011_auto_20150124_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediatype',
            name='base_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
