# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-26 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180825_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballotpaper',
            name='can_add_votes',
            field=models.BooleanField(default=False),
        ),
    ]
