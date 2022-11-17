import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from projectapp.models import Project, Todo


User = get_user_model()


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('projects_num', type=int)

    # def create_projects(self, num: int) -> None:
    #     projects = []
    #     users_count = User.objects.count()
    #     for i in range(num):
    #         new_project = Project(
    #             title=f'Проект_{i}',
    #             url_repo=f'https://github.com/all/project_{i}'
    #         )
    #         projects.append(new_project)

    #     projects = Project.objects.bulk_create(projects)

    #     print(projects)

    #     for project in projects:
    #         users_number = random.randint(2, min(15, users_count))
    #         users_in_project = random.sample(
    #             list(User.objects.all()),
    #             users_number
    #         )
    #         project.users.set(users_in_project)

    # def create_todos(self) -> None:
    #     todos = []
    #     projects = Project.objects.all()
    #     max_todos_per_project = random.randint(1, 15)
    #     users = list(User.objects.all())
    #     for current_project in projects:
    #         for i in range(max_todos_per_project):
    #             author = random.choice(users)
    #             new_todo = Todo(
    #                 project=current_project,
    #                 text=(f'Какой-то текст заметки {i} '
    #                       f'для проекта {current_project}'),
    #                 author=author,
    #                 is_active=True
    #             )
    #             todos.append(new_todo)

    #     Todo.objects.bulk_create(todos)

    def handle(self, *args, **options):
        # Создадим Проекты
        # projects_num = options.get('projects_num')
        Project.objects.all().delete()
        Todo.objects.all().delete()
        users = User.objects.all()

        mixer.cycle(22).blend(Project,
                              users=lambda: random.sample(list(users), 3))

        projects = Project.objects.all()

        mixer.cycle(100).blend(Todo,
                               is_active=True,
                               project=lambda: random.choice(list(projects)),
                               author=lambda: random.choice(list(users)))
        # self.create_projects(projects_num)
        # self.create_todos()
