# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userstore_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstore',
            name='refund_policy',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='userstore',
            name='usage_policy',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
