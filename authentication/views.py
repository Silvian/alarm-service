from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    context = {}
    if request.GET.get('logout', False):
        context['logout'] = True
        context['msg'] = "You've been logged out successfully"

    return render(request, "alarm/login.html", context)


def authenticate_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        context = {}
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(settings.REDIRECT_URL)
            else:
                context['msg'] = "This account has been disabled"
                return render(request, "alarm/login.html", context)
        else:
            # the authentication system was unable to verify the username and password
            context['msg'] = "The username or password is incorrect"
            return render(request, "alarm/login.html", context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/authenticate/login?logout=true')
