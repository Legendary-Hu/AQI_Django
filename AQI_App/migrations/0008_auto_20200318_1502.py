# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-18 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQI_App', '0007_auto_20200318_1455'),
    ]

    operations = [

        migrations.AlterField(
            model_name='city_info',
            name='aqi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data_history',
            name='aqi',
            field=models.IntegerField(null=True),
        ),
    ]
