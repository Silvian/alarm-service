from django.shortcuts import render


"""Views"""


# Index render view
def index_view(request):
    return render(request, "alarm/index.html")
