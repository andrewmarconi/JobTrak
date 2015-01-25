# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0002_company_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyLocation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('address', models.ForeignKey(to='jobtrak_core.Address', null=True)),
                ('company', models.ForeignKey(to='jobtrak_core.Company', null=True)),
            ],
            options={
                'verbose_name': 'Company Location',
                'verbose_name_plural': 'Company Locations',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
    ]
