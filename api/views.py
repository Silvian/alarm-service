
from alarm.models import UserProfile, Log, Alert, AlarmStateConfiguration
from rest_framework import viewsets
from serializers import UserSerializer, LogSerializer, AlertSerializer, AlarmStateConfigurationSerializer


""" ViewSets define the view behavior. """


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class LogViewSet(viewsets.ModelViewSet):

    queryset = Log.objects.all()
    serializer_class = LogSerializer


class AlertViewSet(viewsets.ModelViewSet):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlarmStateConfigurationSet(viewsets.ModelViewSet):

    queryset = AlarmStateConfiguration.objects.all()
    serializer_class = AlarmStateConfigurationSerializer
