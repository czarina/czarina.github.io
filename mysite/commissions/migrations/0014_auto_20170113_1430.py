# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-13 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0013_auto_20170113_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_max_weeks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='time_min_weeks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
