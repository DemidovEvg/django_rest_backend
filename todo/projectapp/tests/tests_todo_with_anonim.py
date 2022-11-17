from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from projectapp.models import Project
from projectapp.models import Todo
from userapp.tests.utils.urls_for_test import UrlsForTest
from userapp.tests.utils.user_fixture import UserFixture
from projectapp.tests.utils.project_fixture import ProjectFixture

User = get_user_model()


class TestTodoWithAnonim(APITestCase):
    def setUp(self):
        self.user_fixture = UserFixture()
        self.projectFixture = ProjectFixture()

    def test_list(self):
        response = self.client.get(UrlsForTest.listTodos)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        project = Project.objects.all().first()
        author = User.objects.all().first()
        data = {
            'project': project.id,
            'text': 'La la la',
            'author': author.id,
            'is_active': True
        }
        response = self.client.post(UrlsForTest.createTodo, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        todo = Todo.objects.all().first()
        response = self.client.get(UrlsForTest.retrieveTodo.format(
            pk=todo.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update(self):
        todo = Todo.objects.all().first()
        data = {
            'text': f'{todo.text}_updated',
        }
        response = self.client.patch(UrlsForTest.partialUpdateTodo.format(
            pk=todo.pk,
            data=data)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update(self):
        todo = Todo.objects.all().first()
        project = Project.objects.all().last()
        author = User.objects.all().last()
        data = {
            'project': project.id,
            'text': 'La la la',
            'author': author.id,
        }
        response = self.client.put(
            UrlsForTest.updateTodo.format(pk=todo.pk),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy(self):
        todo = Todo.objects.all().first()
        response = self.client.delete(
            UrlsForTest.destroyTodo.format(pk=todo.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
