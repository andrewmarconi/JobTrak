# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0012_auto_20150124_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joblisting',
            name='people',
            field=models.ManyToManyField(to='jobtrak_core.Contact'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companylocation',
            name='address',
            field=models.ForeignKey(blank=True, to='jobtrak_core.Address', null=True),
            preserve_default=True,
        ),
    ]
