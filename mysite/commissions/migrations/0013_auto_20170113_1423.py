# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-13 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0012_auto_20161116_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='revisions',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='wont_draw',
            field=models.TextField(blank=True, null=True),
        ),
    ]
