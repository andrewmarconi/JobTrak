# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0005_auto_20150124_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Company Type',
                'verbose_name_plural': 'Company Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ManyToManyField(to='jobtrak_core.CompanyType', null=True, blank=True),
            preserve_default=True,
        ),
    ]
