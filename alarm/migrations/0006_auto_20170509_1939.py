# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-09 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0005_userprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmstateconfiguration',
            old_name='client_state',
            new_name='client_connected_state',
        ),
        migrations.AddField(
            model_name='alarmstateconfiguration',
            name='last_client_connected_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alarmstateconfiguration',
            name='last_notified_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
