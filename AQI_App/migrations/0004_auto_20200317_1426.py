# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-17 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQI_App', '0003_auto_20200317_1403'),
    ]

    operations = [

        migrations.AlterField(
            model_name='city_info',
            name='max_poll',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='data_history',
            name='max_poll',
            field=models.CharField(max_length=50),
        ),
    ]
