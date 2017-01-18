# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0005_auto_20161104_0037'),
        ('orders', '0002_auto_20161103_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='commissions.Product'),
        ),
    ]