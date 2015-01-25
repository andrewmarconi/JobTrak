# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0010_auto_20150124_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='Donny', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='Donny', max_length=128),
            preserve_default=False,
        ),
    ]
