# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0005_auto_20170520_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmstateconfiguration',
            name='alarm_message',
            field=models.TextField(),
        ),
    ]