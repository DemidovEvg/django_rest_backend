import django_filters
from rest_framework import viewsets

from projectapp.models import Project
from projectapp.serializers import ProjectSerializer
from utils.factory_pagination import FactoryPagination


class ProductFilterSet(django_filters.FilterSet):

    class Meta:
        model = Project
        fields = {
            "title": [
                "contains",
            ],
        }


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('title')

    serializer_class = ProjectSerializer

    pagination_class = FactoryPagination.get_pagination(page_size=10)

    filterset_class = ProductFilterSet

    # @action(detail=True, methods=["get"])
    # def get_project_name(self, request, pk=None):
    #     return Response({"name": "privet"})
