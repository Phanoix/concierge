# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailvalidator', '0002_domain_catchall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailregexvalidator',
            name='allow_all',
            field=models.BooleanField(default=False, verbose_name='Allow all from domain'),
        ),
        migrations.AlterField(
            model_name='emailregexvalidator',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name', default='.'),
            preserve_default=False
        ),
        migrations.AlterField(
            model_name='emailregexvalidator',
            name='regex',
            field=models.CharField(max_length=100, verbose_name='Regex/domain'),
        ),
    ]
