from django.urls import include, path
from rest_framework import routers

from projectapp.views import ProjectViewSet
from projectapp.views import TodoViewSet
# from projectapp.views import ProjectUpdateApiView

router = routers.DefaultRouter()

router.register('project', ProjectViewSet)
router.register('todo', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('project/update/<int:pk>', ProjectUpdateApiView.as_view())
]
