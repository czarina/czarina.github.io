# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20161106_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstore',
            name='cover_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/'),
        ),
    ]
