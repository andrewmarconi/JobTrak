# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0018_auto_20150124_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediaaccount',
            name='company',
            field=models.ForeignKey(blank=True, to='jobtrak_core.Company', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialmediaaccount',
            name='company_location',
            field=models.ForeignKey(blank=True, to='jobtrak_core.CompanyLocation', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='contact',
            field=models.ForeignKey(blank=True, to='jobtrak_core.Contact', null=True),
            preserve_default=True,
        ),
    ]
