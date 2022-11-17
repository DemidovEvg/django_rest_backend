from django.urls import include, re_path
from rest_framework import routers
from userapp.views import UserViewSet


router = routers.DefaultRouter()

router.register('user', UserViewSet)
urlpatterns = [
    re_path(r'^(?P<version>\d*)/?', include(router.urls)),
]
