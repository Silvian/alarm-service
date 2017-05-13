from django.shortcuts import render
from alarm.models import UserProfile, Log, AlarmStateConfiguration
from rest_framework import viewsets
from serializers import UserSerializer, LogSerializer, AlarmStateConfigurationSerializer


""" ViewSets define the view behavior. """


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class LogViewSet(viewsets.ModelViewSet):

    queryset = Log.objects.all()
    serializer_class = LogSerializer


class AlarmStateConfigurationSet(viewsets.ModelViewSet):

    queryset = AlarmStateConfiguration.objects.all()
    serializer_class = AlarmStateConfigurationSerializer
