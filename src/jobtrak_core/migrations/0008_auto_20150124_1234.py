# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0007_auto_20150124_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('local_url_data', models.CharField(max_length=128, verbose_name=b'Account')),
                ('contact', models.ForeignKey(to='jobtrak_core.Contact')),
            ],
            options={
                'verbose_name': 'Social Media Account',
                'verbose_name_plural': 'Social Media Accounts',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='SocialMedia',
            new_name='SocialMediaType',
        ),
        migrations.AddField(
            model_name='socialmediaaccount',
            name='social_media_type',
            field=models.ForeignKey(to='jobtrak_core.SocialMediaType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
