from mixer.backend.django import mixer
from projectapp.models import Todo


class ProjectFixture:
    def __init__(self):
        self.create_todos_and_projects()

    def create_todos_and_projects(self):
        mixer.cycle(10).blend(Todo)
