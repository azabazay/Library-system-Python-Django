# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-05 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0011_auto_20171206_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/categories/None/no-img.jpg', upload_to='images/categories/'),
        ),
    ]
