from django.contrib.auth.decorators import login_required
from django.shortcuts import render


"""Views"""


# Index render view
@login_required
def index_view(request):
    return render(request, "alarm/index.html")


@login_required
def users_view(request):
    return render(request, "alarm/users.html")
