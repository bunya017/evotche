# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180522_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ballotpaper',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='ballotpaper',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='ballotpaper',
            name='stop_date',
        ),
        migrations.RemoveField(
            model_name='ballotpaper',
            name='stop_time',
        ),
        migrations.AddField(
            model_name='ballotpaper',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ballotpaper',
            name='open_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
