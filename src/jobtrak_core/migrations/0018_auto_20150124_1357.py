# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0017_auto_20150124_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('order_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Job Status',
                'verbose_name_plural': 'Job Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='ref_by',
            field=models.ForeignKey(verbose_name='Referred By', blank=True, to='jobtrak_core.Contact', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joblisting',
            name='sourceURL',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joblisting',
            name='status',
            field=models.ForeignKey(blank=True, to='jobtrak_core.JobStatus', null=True),
            preserve_default=True,
        ),
    ]
