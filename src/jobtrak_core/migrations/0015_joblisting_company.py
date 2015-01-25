# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0014_auto_20150124_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='company',
            field=models.ForeignKey(blank=True, to='jobtrak_core.CompanyLocation', null=True),
            preserve_default=True,
        ),
    ]
