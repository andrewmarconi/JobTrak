# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0003_auto_20150124_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name=b'Postal Code', blank=True),
            preserve_default=True,
        ),
    ]
