from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/all/', views.list_users, name='all_users'),
    url(r'^users/get/', views.get_user, name='get_user'),
    url(r'^users/add/', views.add_user, name='add_user'),
    url(r'^users/update/', views.update_user, name='update_user'),
    url(r'^users/delete/', views.delete_user, name='delete_user'),
    url(r'^users/', views.users_view, name='users'),
    url(r'^logs/get/today/', views.get_logs_today, name='today_logs'),
    url(r'^logs/get', views.get_logs_date, name='date_logs'),
    url(r'^logs/', views.logs_view, name='logs'),
    url(r'^config/status/get/', views.get_config_status, name='alarm_status_get'),
    url(r'^config/status/update/', views.update_alarm_status, name='alarm_status_update'),
    url(r'^$', views.index_view, name='dashboard'),
]
