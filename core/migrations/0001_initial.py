# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('guid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('accepted_terms', models.BooleanField(default=False)),
                ('receives_newsletter', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
