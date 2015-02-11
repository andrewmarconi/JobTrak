# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('when', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='When', blank=True)),
                ('note', models.TextField(default=b'', verbose_name='Note', blank=True)),
            ],
            options={
                'get_latest_by': 'when',
                'verbose_name': 'History Item',
                'verbose_name_plural': 'History Items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('sourceURL', models.URLField(null=True, blank=True)),
                ('date_posted', models.DateField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('company', models.ForeignKey(blank=True, to='contact.CompanyLocation', null=True)),
                ('ref_by', models.ForeignKey(verbose_name='Referred By', blank=True, to='contact.Contact', null=True)),
            ],
            options={
                'verbose_name': 'Job Listing',
                'verbose_name_plural': 'Job Listings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobListingPerson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('note', models.CharField(max_length=255, null=True, verbose_name='Note', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', to='contact.Contact')),
                ('joblisting', models.ForeignKey(verbose_name='Job Listing', to='core.JobListing')),
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
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('order_id', models.IntegerField(verbose_name='Order')),
            ],
            options={
                'ordering': ['order_id'],
                'verbose_name': 'Job Status',
                'verbose_name_plural': 'Job Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='joblistingperson',
            name='role',
            field=models.ForeignKey(verbose_name='Role', to='core.JobListingRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joblisting',
            name='status',
            field=models.ForeignKey(blank=True, to='core.JobStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='joblisting',
            field=models.ForeignKey(verbose_name='Job Listing', blank=True, to='core.JobListing', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='who',
            field=models.ForeignKey(verbose_name='Contact', blank=True, to='contact.Contact', null=True),
            preserve_default=True,
        ),
    ]
