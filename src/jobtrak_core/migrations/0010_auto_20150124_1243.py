# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0009_contact_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
