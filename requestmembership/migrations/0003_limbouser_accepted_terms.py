# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-17 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestmembership', '0002_limbouser'),
    ]

    operations = [
        migrations.AddField(
            model_name='limbouser',
            name='accepted_terms',
            field=models.BooleanField(default=False),
        ),
    ]
