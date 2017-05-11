from alarm.models import UserProfile
from rest_framework import serializers


""" Django rest framework serizliers. """


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'mobile')
