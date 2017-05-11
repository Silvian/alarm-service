from django.shortcuts import render
from alarm.models import UserProfile
from rest_framework import viewsets
from serializers import UserSerializer


""" ViewSets define the view behavior. """


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
