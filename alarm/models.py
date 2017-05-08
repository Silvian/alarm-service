from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

"""Alarm models"""

DOOR_STATUS = (
    ('0', 'open'),
    ('1', 'closed'),
)

ALARM_STATUS = (
    ('0', 'off'),
    ('1', 'on'),
)

CLIENT_STATUS = (
    ('0', 'disconnected'),
    ('1', 'connected'),
)


class Log(models.Model):

    time_stamp = models.DateTimeField()
    door_state = models.CharField(max_length=1, choices=DOOR_STATUS)
    alarm_state = models.CharField(max_length=1, choices=ALARM_STATUS)
    client_state = models.CharField(max_length=1, choices=CLIENT_STATUS)

    def publish(self):
        self.time_stamp = timezone.now()
        self.save()

    def __str__(self):
        return self.time_stamp


class AlarmStateConfiguration(models.Model):
    alarm_name = models.CharField(primary_key=True, max_length=20, null=False)
    alarm_state = models.CharField(max_length=1, choices=ALARM_STATUS)
    client_state = models.CharField(max_length=1, choices=CLIENT_STATUS)

    def publish(self):
        self.save()

    def __str__(self):
        return self.alarm_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', null=False)
    mobile = models.CharField(max_length=200, null=False, blank=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.user.name
