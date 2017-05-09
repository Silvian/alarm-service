import json
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from alarm.forms import UserProfileForm
from alarm.models import UserProfile


"""Views"""

SUCCESS_RESPONSE = {'success': True}


# Index render view
@login_required
def index_view(request):
    return render(request, "alarm/index.html")


@login_required
def users_view(request):
    return render(request, "alarm/users.html")


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
