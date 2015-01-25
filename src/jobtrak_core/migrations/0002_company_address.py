# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.ForeignKey(to='jobtrak_core.Address', null=True),
            preserve_default=True,
        ),
    ]
