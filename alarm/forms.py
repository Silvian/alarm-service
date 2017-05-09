from django import forms
from models import UserProfile


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'mobile')
