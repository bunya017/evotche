# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 22:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BallotPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballot_name', models.CharField(max_length=50)),
                ('ballot_url', models.SlugField(unique=True)),
                ('is_photo_ballot', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('has_free_tokens', models.BooleanField(default=False)),
                ('open_date', models.DateTimeField(blank=True, null=True)),
                ('close_date', models.DateTimeField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('email_delivery', models.BooleanField(default=False)),
                ('text_delivery', models.BooleanField(default=False)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Ballot Papers',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250)),
                ('ballot_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.BallotPaper')),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, upload_to='uploads/')),
                ('votes', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Choices',
            },
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('category', 'choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('ballot_paper', 'category_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='ballotpaper',
            unique_together=set([('ballot_name', 'created_by')]),
        ),
    ]
