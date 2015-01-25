# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0013_auto_20150124_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListingPerson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('contact', models.ForeignKey(to='jobtrak_core.Contact')),
                ('joblisting', models.ForeignKey(to='jobtrak_core.JobListing')),
            ],
            options={
                'verbose_name': 'Associated Person',
                'verbose_name_plural': 'Associated People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobListingRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='joblistingperson',
            name='role',
            field=models.ForeignKey(to='jobtrak_core.JobListingRole'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='actionhistory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='joblisting',
            name='people',
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='joblisting',
            field=models.ForeignKey(blank=True, to='jobtrak_core.JobListing', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='note',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='when',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='who',
            field=models.ForeignKey(blank=True, to='jobtrak_core.Contact', null=True),
            preserve_default=True,
        ),
    ]
