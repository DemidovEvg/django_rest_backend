from rest_framework import status
from rest_framework.test import (APIRequestFactory,
                                 force_authenticate,
                                 APITestCase)
from django.contrib.auth import get_user_model
from projectapp.models import Project
from projectapp.views import ProjectViewSet
from userapp.tests.utils.urls_for_test import UrlsForTest
from userapp.tests.utils.user_fixture import UserFixture
from projectapp.tests.utils.project_fixture import ProjectFixture

User = get_user_model()


class TestProjectWithAdmin(APITestCase):
    def setUp(self):
        self.user_fixture = UserFixture()
        self.admin = self.user_fixture.admin

        self.projectFixture = ProjectFixture()

        self.factory = APIRequestFactory()

    def test_list(self):
        request = self.factory.get(UrlsForTest.listProjects)
        force_authenticate(request, self.admin)
        response = ProjectViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        user = User.objects.all().first()
        data = {
            'title': 'La la la',
            'users': [user.id]
        }
        request = self.factory.post(UrlsForTest.createProject,
                                    data,
                                    format='json')

        force_authenticate(request, self.admin)

        response = ProjectViewSet.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        project = Project.objects.all().first()
        request = self.factory.get(
            UrlsForTest.retrieveProject.format(pk=project.pk)
        )
        force_authenticate(request, self.admin)
        response = ProjectViewSet.as_view({'get': 'retrieve'})(
            request,
            pk=project.pk
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        project = Project.objects.all().first()
        data = {
            'title': f'{project.title}_updated',
        }
        request = self.factory.patch(
            UrlsForTest.partialUpdateProject.format(pk=project.pk),
            data=data,
            format='json'
        )
        force_authenticate(request, self.admin)
        response = ProjectViewSet.as_view({'patch': 'update'})(
            request,
            pk=project.pk,
            partial=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        project = Project.objects.all().first()
        user = User.objects.all().first()
        data = {
            'title': 'La la la',
            'users': [user.id]
        }
        request = self.factory.patch(
            UrlsForTest.partialUpdateProject.format(pk=project.pk),
            data=data,
            format='json'
        )
        force_authenticate(request, self.admin)
        response = ProjectViewSet.as_view({'patch': 'update'})(
            request,
            pk=project.pk,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy(self):
        project = Project.objects.all().first()
        request = self.factory.delete(
            UrlsForTest.partialUpdateProject.format(pk=project.pk)
        )
        force_authenticate(request, self.admin)
        response = ProjectViewSet.as_view({'delete': 'destroy'})(
            request,
            pk=project.pk,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
