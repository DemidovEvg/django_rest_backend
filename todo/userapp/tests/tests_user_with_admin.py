from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from userapp.tests.utils.urls_for_test import UrlsForTest
from userapp.tests.utils.user_fixture import UserFixture
from userapp.tests.utils import headers

User = get_user_model()


class TestUserWithAdmin(APITestCase):
    def setUp(self):
        self.user_fixture = UserFixture()

    def test_list(self):
        response = self.client.get(UrlsForTest.listUsers,
                                   **headers.admin_headers(self.client))
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        self.assertTrue(len(response.data))

    def test_create(self):
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'user_email@email.ru',
        }
        response = self.client.post(UrlsForTest.createUser,
                                    format='json',
                                    data=data,
                                    **headers.admin_headers(self.client))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve(self):
        user_for_retrieve = self.user_fixture.admin
        response = self.client.get(
            UrlsForTest.retrieveUser.format(pk=user_for_retrieve.pk),
            **headers.admin_headers(self.client)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        user_for_update = self.user_fixture.admin
        data = {
            'email': 'new_email@mail.ru',
        }
        response = self.client.patch(
            UrlsForTest.partialUpdateUser.format(pk=user_for_update.pk),
            data=data,
            **headers.admin_headers(self.client)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'],
                         'new_email@mail.ru')

    def test_update(self):
        user_for_update = self.user_fixture.admin
        data = {
            'email': 'new_email@mail.ru',
        }
        response = self.client.put(
            UrlsForTest.updateUser.format(pk=user_for_update.pk),
            data=data,
            **headers.admin_headers(self.client)
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0].code, "required")

    def test_destroy(self):
        user_for_destroy = self.user_fixture.admin
        response = self.client.delete(
            UrlsForTest.destroyUser.format(pk=user_for_destroy.pk),
            **headers.admin_headers(self.client)
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
