from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from alerts import SMSAlert
from django.utils import timezone

from django.db import models

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


class AlarmStateConfiguration(models.Model):

    alarm_name = models.CharField(
        primary_key=True,
        max_length=20,
        null=False
    )
    alarm_status = models.CharField(
        max_length=1,
        choices=ALARM_STATUS
    )
    last_notified_time = models.DateTimeField(
        null=True,
        blank=True
    )
    client_connected_state = models.CharField(
        max_length=1,
        choices=CLIENT_STATUS
    )
    last_client_connected_time = models.DateTimeField(
        null=True,
        blank=True
    )
    alarm_message = models.TextField(
        null=False,
        blank=False
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.alarm_name


class Alert(models.Model):

    type = models.CharField(
        max_length=10,
        null=False,
        default='SMS'
    )
    sent = models.PositiveIntegerField(
        verbose_name='messages sent',
        default=0
    )
    remaining = models.PositiveIntegerField(
        verbose_name='messages remaining',
        default=0
    )
    message_id = models.CharField(
        verbose_name='message ID',
        max_length=200,
        null=True,
        blank=True,
    )
    time = models.DateTimeField()

    class Meta:
        get_latest_by = "time"

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return "{} - {}".format(
            self.type, self.time
        )


class Log(models.Model):
    time_stamp = models.DateTimeField()
    door_state = models.CharField(
        max_length=1,
        choices=DOOR_STATUS
    )
    alarm_state = models.CharField(
        max_length=1,
        choices=ALARM_STATUS,
        blank=True
    )
    client_state = models.CharField(
        max_length=1,
        choices=CLIENT_STATUS,
        blank=True
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.time_stamp.strftime(
            settings.DATE_TIME_FORMAT
        )


class UserProfile(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    mobile = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


def _log_alert(response):

    sent = 1

    if Alert.objects.all():
        last_alert = Alert.objects.latest()
        sent = last_alert.sent + 1

    text_id = 0
    remaining = 0

    if response['success']:
        text_id = response['textId']
        remaining = response['quotaRemaining']

    new_alert = Alert(type='SMS',
                      sent=sent,
                      remaining=remaining,
                      message_id=text_id,
                      )

    new_alert.publish()


def send_alerts_to_users(alarm_state, client_state):
    if alarm_state == '1' or client_state == '0':
        alert = SMSAlert()
        users = UserProfile.objects.all()
        for user in users:
            response = alert.send_alert(AlarmStateConfiguration.objects.get(
                alarm_name=settings.ALARM_NAME).alarm_message, user.mobile)
            _log_alert(response)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(pre_save, sender=Log)
def set_alarm_states(sender, instance, *args, **kwargs):
    instance.alarm_state = AlarmStateConfiguration.objects.get(
                                alarm_name=settings.ALARM_NAME).alarm_status

    instance.client_state = AlarmStateConfiguration.objects.get(
                                alarm_name=settings.ALARM_NAME).client_connected_state


@receiver(post_save, sender=Log)
def send_alerts(sender, instance=None, created=False, **kwargs):
    send_alerts_to_users(instance.alarm_state, instance.client_state)
