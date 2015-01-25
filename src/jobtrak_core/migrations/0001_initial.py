# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'History Item',
                'verbose_name_plural': 'History Items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line1', models.CharField(max_length=45, verbose_name=b'Address line 1')),
                ('address_line2', models.CharField(max_length=45, verbose_name=b'Address line 2', blank=True)),
                ('postal_code', models.CharField(max_length=10, verbose_name=b'Postal Code')),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=40, verbose_name=b'State/Province', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Contact Type',
                'verbose_name_plural': 'Contact Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['name', 'iso_code'],
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Job Listing',
                'verbose_name_plural': 'Job Listings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StateProvince',
            fields=[
                ('iso_code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('country', models.ForeignKey(to='jobtrak_core.Country')),
            ],
            options={
                'verbose_name': 'State or province',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_type',
            field=models.ForeignKey(to='jobtrak_core.ContactType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(to='jobtrak_core.Country'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('address_line1', 'address_line2', 'postal_code', 'city', 'state_province', 'country')]),
        ),
    ]
