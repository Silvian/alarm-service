from django import forms
from models import UserProfile, AlarmStateConfiguration


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'mobile')


class AlarmStateConfigurationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlarmStateConfigurationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AlarmStateConfiguration
        fields = ('alarm_name', 'alarm_status', 'client_connected_state')
