# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-04-01 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQI_App', '0009_auto_20200324_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=16)),
                ('content', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),

    ]