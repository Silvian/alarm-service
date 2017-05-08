from django.contrib import admin

from .models import Log, AlarmStateConfiguration, UserProfile

admin.site.register(AlarmStateConfiguration)
admin.site.register(Log)
admin.site.register(UserProfile)
