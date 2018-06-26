# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-05 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lib', '0002_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, help_text='Comment', verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title', max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Description')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, help_text='PDF', null=True, upload_to='documents/', verbose_name='PDF'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, help_text='Title', max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lib.Thread'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]