# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-04 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, help_text='Description', verbose_name='Description'),
        ),
    ]