from django.contrib import admin

from .models import Log, Alert, AlarmStateConfiguration, UserProfile

admin.site.register(AlarmStateConfiguration)
admin.site.register(Log)
admin.site.register(UserProfile)
admin.site.register(Alert)
