# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-05 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/users/None/no-img.jpg', upload_to='images/users/'),
        ),
    ]
