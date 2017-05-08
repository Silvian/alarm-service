from django.contrib import admin

from .models import Log, AlarmStateConfiguration

admin.site.register(AlarmStateConfiguration)
admin.site.register(Log)
