# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0006_auto_20170525_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmstateconfiguration',
            name='alarm_name',
            field=models.CharField(default='primary', max_length=20, primary_key=True, serialize=False),
        ),
    ]
