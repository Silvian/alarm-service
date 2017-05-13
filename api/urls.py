from django.conf.urls import url, include
from rest_framework import routers
from views import UserProfileViewSet, LogViewSet, AlarmStateConfigurationSet


""" Routers provide an easy way of automatically determining the URL conf. """


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'log', LogViewSet)
router.register(r'configuration', AlarmStateConfigurationSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
