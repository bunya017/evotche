# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ballotpaper',
            old_name='email_delivery',
            new_name='has_email_delivery',
        ),
        migrations.RenameField(
            model_name='ballotpaper',
            old_name='is_paid',
            new_name='has_paid_tokens',
        ),
        migrations.RenameField(
            model_name='ballotpaper',
            old_name='text_delivery',
            new_name='has_text_delivery',
        ),
        migrations.RenameField(
            model_name='ballotpaper',
            old_name='is_open',
            new_name='is_protected_with_tokens',
        ),
    ]
