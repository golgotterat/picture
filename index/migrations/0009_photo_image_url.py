# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180614_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
