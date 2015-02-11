# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebLinkAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('local_url_data', models.CharField(max_length=128, verbose_name='Account')),
                ('company', models.ForeignKey(verbose_name='Company', blank=True, to='contact.Company', null=True)),
                ('company_location', models.ForeignKey(verbose_name='Company Location', blank=True, to='contact.CompanyLocation', null=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', blank=True, to='contact.Contact', null=True)),
            ],
            options={
                'verbose_name': 'Web Link Account',
                'verbose_name_plural': 'Web Link Accounts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebLinkType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('note', models.CharField(max_length=255, null=True, verbose_name='Note', blank=True)),
                ('base_url', models.URLField(null=True, verbose_name=b'Base URL', blank=True)),
            ],
            options={
                'verbose_name': 'Web Link Type',
                'verbose_name_plural': 'Web Link Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='weblinkaccount',
            name='web_link_type',
            field=models.ForeignKey(to='links.WebLinkType'),
            preserve_default=True,
        ),
    ]
