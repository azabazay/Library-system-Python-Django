# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-06 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0012_auto_20171206_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.ManyToManyField(related_name='books', to='lib.Location'),
        ),
    ]
