# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-09 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0002_auto_20210309_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='stickers',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
