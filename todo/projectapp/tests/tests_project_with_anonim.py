from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from projectapp.models import Project
from userapp.tests.utils.urls_for_test import UrlsForTest
from userapp.tests.utils.user_fixture import UserFixture
from projectapp.tests.utils.project_fixture import ProjectFixture

User = get_user_model()


class TestProjectWithAnonim(APITestCase):
    def setUp(self):
        self.user_fixture = UserFixture()
        self.projectFixture = ProjectFixture()

    def test_list(self):
        response = self.client.get(UrlsForTest.listProjects)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        user = User.objects.all().first()
        data = {
            'title': 'La la la',
            'users': [user.id]
        }
        response = self.client.post(UrlsForTest.createProject, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        project = Project.objects.all().first()
        response = self.client.get(
            UrlsForTest.retrieveProject.format(pk=project.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update(self):
        project = Project.objects.all().first()
        data = {
            'title': f'{project.title}_updated',
        }
        response = self.client.patch(
            UrlsForTest.partialUpdateProject.format(pk=project.pk),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update(self):
        project = Project.objects.all().first()
        user = User.objects.all().first()
        data = {
            'title': 'La la la',
            'users': [user.id]
        }
        response = self.client.put(
            UrlsForTest.updateProject.format(pk=project.pk),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy(self):
        project = Project.objects.all().first()
        response = self.client.delete(
            UrlsForTest.destroyProject.format(pk=project.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
