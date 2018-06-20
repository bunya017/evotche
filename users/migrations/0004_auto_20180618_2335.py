# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_new_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='payant_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
