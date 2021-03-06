# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-05 16:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 12, 5, 16, 39, 51, 826398, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
