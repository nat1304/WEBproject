# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecter', '0004_auto_20161222_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='capacity',
            field=models.TextField(blank=True, verbose_name='Объём'),
        ),
        migrations.AddField(
            model_name='product',
            name='interface',
            field=models.TextField(blank=True, verbose_name='Интерфейс'),
        ),
    ]
