from userapp.tests.utils.user_fixture import UserFixture
from userapp.tests.utils.urls_for_test import UrlsForTest


def token(client, login, password):
    data = {
        "username": login,
        "password": password,
    }
    response = client.post(UrlsForTest.retrieveToken,
                           format='json',
                           data=data)
    token = response.data['access']
    return token


def admin_headers(client):
    admin_token = token(client,
                        UserFixture.admin_login,
                        UserFixture.admin_password)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {admin_token}"
    }
    return headers


def developer_headers(client):
    developer_token = token(client,
                            UserFixture.developer_login,
                            UserFixture.developer_password)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {developer_token}"
    }
    return headers


def owner_headers(client):
    owner_token = token(client,
                        UserFixture.owner_login,
                        UserFixture.owner_password)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {owner_token}"
    }
    return headers
