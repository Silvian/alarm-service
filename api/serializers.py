from alarm.models import UserProfile, Log, Alert, AlarmStateConfiguration
from rest_framework import serializers


""" Django rest framework serizliers. """


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'mobile')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ('time_stamp', 'door_state')


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('type', 'sent', 'remaining', 'time')


class AlarmStateConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlarmStateConfiguration
        fields = ('alarm_name', 'alarm_status',
                  'last_notified_time', 'client_connected_state',
                  'last_client_connected_time')
