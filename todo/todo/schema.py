import datetime

import graphene
from graphene_django import DjangoObjectType
from graphene_django import filter
from userapp.models import User
from projectapp.models import Todo, Project


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # fields = '__all__'
        filter_fields = {
            'username': ['exact', 'icontains']
        }
        interfaces = [graphene.relay.Node]


class ProjectGrapheneType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'
        filter_fields = {
            'title': ['exact', 'icontains']
        }


class TodoGrapheneType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    users = filter.DjangoFilterConnectionField(UserNode)

    todos = graphene.List(TodoGrapheneType)
    todo_by_id = graphene.Field(TodoGrapheneType,
                                id=graphene.ID(required=True))
    todos_by_date = graphene.List(
        TodoGrapheneType,
        date_start=graphene.Date(required=False),
        date_end=graphene.Date(required=False)
    )

    projects = graphene.List(ProjectGrapheneType)
    project_by_id = graphene.Field(ProjectGrapheneType,
                                   id=graphene.ID(required=True))
    projects_by_title = graphene.List(ProjectGrapheneType,
                                      title=graphene.String(required=True))

    def resolve_todos(root, info: dict):
        return Todo.objects.all()

    def resolve_todo_by_id(root, info: dict, id: int):
        return Todo.objects.get(id=id)

    def resolve_todos_by_date(root,
                              info: dict,
                              date_start: datetime.date | None = None,
                              date_end: datetime.date | None = None):
        return Todo.objects.filter(
            created_at__gte=date_start,
            created_at__lte=date_end
        )

    def resolve_projects(root, info: dict):
        return Project.objects.all()

    def resolve_project_by_id(root, info: dict, id: int):
        return Project.objects.get(id=id)

    def resolve_projects_by_title(root, info: dict, title: str):
        return Project.objects.filter(title__contains=title)


schema = graphene.Schema(query=Query)
