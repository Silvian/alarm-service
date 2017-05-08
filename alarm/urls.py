from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/', views.users_view, name='users'),
    url(r'^logs/', views.index_view, name='logs'),
    url(r'^$', views.index_view, name='dashboard'),
]
