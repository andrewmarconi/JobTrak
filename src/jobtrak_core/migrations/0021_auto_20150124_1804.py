# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0020_auto_20150124_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobstatus',
            options={'ordering': ['order_id'], 'verbose_name': 'Job Status', 'verbose_name_plural': 'Job Statuses'},
        ),
        migrations.AddField(
            model_name='joblistingperson',
            name='note',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobstatus',
            name='order_id',
            field=models.IntegerField(verbose_name=b'Order'),
            preserve_default=True,
        ),
    ]
