# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-21 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_can_review_dubious'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(
                choices=[('H', 'Hacker'), ('M', 'Mentor'), ('S', 'Sponsor'), ('V', 'Volunteer'), ('O', 'Organizer')],
                default='H', max_length=2),
        ),
        migrations.RunSQL(["UPDATE user_user SET type='V' where is_volunteer;"]),
        migrations.RunSQL(["UPDATE user_user SET type='O' where is_organizer;"]),
        migrations.RemoveField(
            model_name='user',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_volunteer',
        ),
    ]
