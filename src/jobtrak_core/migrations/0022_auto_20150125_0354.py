# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0021_auto_20150124_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionhistory',
            options={'get_latest_by': 'when', 'verbose_name': 'History Item', 'verbose_name_plural': 'History Items'},
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='joblisting',
            field=models.ForeignKey(verbose_name=b'Job Listing', blank=True, to='jobtrak_core.JobListing', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='note',
            field=models.TextField(default=b'', verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='when',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'When', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='who',
            field=models.ForeignKey(verbose_name=b'Contact', blank=True, to='jobtrak_core.Contact', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='joblistingperson',
            name='contact',
            field=models.ForeignKey(verbose_name=b'Contact', to='jobtrak_core.Contact'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='joblistingperson',
            name='joblisting',
            field=models.ForeignKey(verbose_name=b'Job Listing', to='jobtrak_core.JobListing'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='joblistingperson',
            name='note',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='joblistingperson',
            name='role',
            field=models.ForeignKey(verbose_name=b'Role', to='jobtrak_core.JobListingRole'),
            preserve_default=True,
        ),
    ]
