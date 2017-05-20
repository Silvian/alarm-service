import json
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from alarm.forms import UserProfileForm, AlarmStateConfigurationForm
from alarm.models import UserProfile, Log, Alert, AlarmStateConfiguration


"""Views"""

SUCCESS_RESPONSE = {'success': True}


# Index render view
@login_required
def index_view(request):
    return render(request, "alarm/index.html")


@login_required
def logs_view(request):
    return render(request, "alarm/logs.html")


@login_required
def users_view(request):
    return render(request, "alarm/users.html")


@login_required
def alerts_view(request):
    return render(request, "alarm/alerts.html")


@login_required
def list_users(request):
    if request.is_ajax:
        users = UserProfile.objects.all()
        data = serializers.serialize("json", users)
        return HttpResponse(data,
                            content_type='application/json')


@login_required
def get_user(request):
    if request.is_ajax:
        user = UserProfile.objects.get(pk=request.GET['id'])
    data = serializers.serialize("json", [user])
    return HttpResponse(data,
                        content_type='application/json')


@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        form.save()
        return HttpResponse(json.dumps(SUCCESS_RESPONSE),
                            content_type='application/json')


@login_required
def update_user(request):
    if request.method == 'POST':
        user = get_object_or_404(UserProfile, id=request.POST['id'])
        form = UserProfileForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(SUCCESS_RESPONSE), content_type='application/json')


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(pk=request.POST['id'])
        user.delete()
        return HttpResponse(json.dumps(SUCCESS_RESPONSE), content_type='application/json')


@login_required
def get_logs_today(request):
    if request.is_ajax:
        logs = Log.objects.filter(time_stamp__date=datetime.date.today())
        data = serializers.serialize("json", logs)
        return HttpResponse(data,
                            content_type='application/json')


@login_required
def get_logs_date(request):
    if request.is_ajax:
        logs = Log.objects.filter(time_stamp__date=request.GET['date'])
        data = serializers.serialize("json", logs)
        return HttpResponse(data,
                            content_type='application/json')


@login_required
def get_config_status(request):
    if request.is_ajax:
        config = AlarmStateConfiguration.objects.filter(alarm_name=settings.ALARM_NAME)
        data = serializers.serialize("json", config)
        return HttpResponse(data,
                            content_type='application/json')


@login_required
def update_alarm_status(request):
    if request.method == 'POST':
        alarm = get_object_or_404(AlarmStateConfiguration, alarm_name=request.POST['alarm_name'])
        form = AlarmStateConfigurationForm(request.POST or None, instance=alarm)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(SUCCESS_RESPONSE), content_type='application/json')


@login_required
def get_alerts_status(request):
    if request.is_ajax:
        if Alert.objects.all():
            alerts = Alert.objects.latest()
            data = serializers.serialize("json", [alerts])
        else:
            data = serializers.serialize("json", [])
        return HttpResponse(data,
                            content_type='application/json')
