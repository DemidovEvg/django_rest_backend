import django_filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from utils.factory_pagination import FactoryPagination

from projectapp.models import Todo
from projectapp.serializers import TodoSerializer


class TodoFilterSet(django_filters.FilterSet):
    project__title__contains = django_filters.CharFilter(
        field_name='project',
        lookup_expr='title__contains'
    )

    created_at__gte = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
        label="От даты или даты и времени (варианты ввода: 08.10.2022, 08.10.2022 12:46, 08.10.2022 12:46:59)",
        input_formats=["%d.%m.%Y", "%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"]
    )

    created_at__lte = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
        label="До даты или даты и времени (варианты ввода: 08.10.2022, 08.10.2022 12:46, 08.10.2022 12:46:59)",
        input_formats=["%d.%m.%Y", "%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"]
    )

    class Meta:
        model = Todo
        fields = ['project__title__contains',
                  'created_at__gte',
                  'created_at__lte']


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(is_active=True).order_by('project__title')

    serializer_class = TodoSerializer

    pagination_class = FactoryPagination.get_pagination(page_size=200)

    filterset_class = TodoFilterSet

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        data_with_author = dict(request.data)
        data_with_author['author'] = request.user.id
        data_with_author['is_active'] = True
        serializer = self.get_serializer(data=data_with_author)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
