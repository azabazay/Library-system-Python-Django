# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-05 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0007_category_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='images/'),
        ),
    ]
