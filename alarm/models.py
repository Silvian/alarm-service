from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
        return self.time_stamp.strftime(settings.DATE_TIME_FORMAT)


class AlarmStateConfiguration(models.Model):
    alarm_name = models.CharField(primary_key=True, max_length=20, null=False)
    alarm_state = models.CharField(max_length=1, choices=ALARM_STATUS)
    last_notified_time = models.DateTimeField(null=True, blank=True)
    client_connected_state = models.CharField(max_length=1, choices=CLIENT_STATUS)
    last_client_connected_time = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.alarm_name


class UserProfile(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    mobile = models.CharField(max_length=200, null=False, blank=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
