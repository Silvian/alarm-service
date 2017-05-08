from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile


"""Views"""


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
        return HttpResponse(data, content_type='application/json')
