# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20161104_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_update_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
