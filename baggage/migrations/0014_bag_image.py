# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-09-16 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baggage', '0013_auto_20180916_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='baggage'),
        ),
    ]
