# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshdesk', '0005_auto_20180917_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='secret_key',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.RunSQL([('INSERT INTO freshdesk_configuration (url, secret_key, \'default\') values (%s, %s, %s)', ['https://gccollab.gctools-outilsgc.ca/', '', True])])
    ]
