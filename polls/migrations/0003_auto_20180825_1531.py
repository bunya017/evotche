# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180825_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ballotpaper',
            old_name='is_protected_with_tokens',
            new_name='is_custom',
        ),
    ]
