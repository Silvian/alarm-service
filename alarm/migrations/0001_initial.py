# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmStateConfiguration',
            fields=[
                ('alarm_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('alarm_status', models.CharField(choices=[('0', 'off'), ('1', 'on')], max_length=1)),
                ('last_notified_time', models.DateTimeField(blank=True, null=True)),
                ('client_connected_state', models.CharField(choices=[('0', 'disconnected'), ('1', 'connected')], max_length=1)),
                ('last_client_connected_time', models.DateTimeField(blank=True, null=True)),
                ('alarm_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('door_state', models.CharField(choices=[('0', 'open'), ('1', 'closed')], max_length=1)),
                ('alarm_state', models.CharField(blank=True, choices=[('0', 'off'), ('1', 'on')], max_length=1)),
                ('client_state', models.CharField(blank=True, choices=[('0', 'disconnected'), ('1', 'connected')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
            ],
        ),
    ]
