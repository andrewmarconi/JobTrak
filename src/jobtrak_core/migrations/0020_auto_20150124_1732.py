# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0019_auto_20150124_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stateprovince',
            name='country',
        ),
        migrations.DeleteModel(
            name='StateProvince',
        ),
    ]
