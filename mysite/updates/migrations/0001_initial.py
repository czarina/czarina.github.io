# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 06:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0008_order_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_userstore_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=100)),
                ('rating_quality', models.DecimalField(decimal_places=1, default=0.0, max_digits=100)),
                ('rating_communication', models.DecimalField(decimal_places=1, default=0.0, max_digits=100)),
                ('rating_professionalism', models.DecimalField(decimal_places=1, default=0.0, max_digits=100)),
                ('rating_timeliness', models.DecimalField(decimal_places=1, default=0.0, max_digits=100)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserStore')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('update_type', models.CharField(choices=[('Request Created', 'Request Created'), ('Request Accepted', 'Request Accepted'), ('Work In Progress', 'Work In Progress'), ('Revision', 'Revision'), ('Chat', 'Chat'), ('Completed', 'Completed'), ('Blog post', 'Blog post'), ('Store announcement', 'Store announcement')], default='Request Created', max_length=120)),
                ('sender_is_artist', models.BooleanField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserStore')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_type', models.CharField(choices=[('Reference', 'Reference'), ('Work in Progress', 'Work in Progress'), ('Final Product', 'Final Product')], default='Reference', max_length=120)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserStore')),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updates.Update')),
            ],
        ),
    ]
