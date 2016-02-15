# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 14:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(unique_for_date='publish', verbose_name='slug')),
                ('body', models.TextField(verbose_name='body')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='publish')),
            ],
            options={
                'db_table': 'simple_articles',
                'ordering': ('-publish',),
            },
        ),
    ]
