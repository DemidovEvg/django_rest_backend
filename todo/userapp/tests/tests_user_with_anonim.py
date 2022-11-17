from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from userapp.tests.utils.urls_for_test import UrlsForTest
from userapp.tests.utils.user_fixture import UserFixture

User = get_user_model()


class TestUserWithAnonim(APITestCase):
    def setUp(self):
        self.user_fixture = UserFixture()

    def test_list(self):
        response = self.client.get(UrlsForTest.listUsers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'user_email@email.ru'
        }
        response = self.client.post(UrlsForTest.createUser, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        user_for_retrieve = self.user_fixture.admin
        response = self.client.get(UrlsForTest.retrieveUser.format(
            pk=user_for_retrieve.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update(self):
        user_for_update = self.user_fixture.admin
        data = {
            'username': f'{user_for_update.username}_updated',
        }
        response = self.client.patch(UrlsForTest.partialUpdateUser.format(
            pk=user_for_update.pk,
            data=data)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update(self):
        user_for_update = self.user_fixture.admin
        data = {
            'username': f'{user_for_update.username}_updated',
        }
        response = self.client.put(UrlsForTest.updateUser.format(
            pk=user_for_update.pk,
            data=data)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy(self):
        user_for_destroy = self.user_fixture.admin
        response = self.client.delete(UrlsForTest.destroyUser.format(
            pk=user_for_destroy.pk)
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
