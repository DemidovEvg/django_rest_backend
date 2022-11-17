# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.db.models import Q

from userapp.models import User


class UserFixture:
    superuser_login = 'superuser'
    superuser_password = 'superuser'
    superuser_email = 'superuser@mail.ru'

    admin_login = 'admin'
    admin_password = 'admin'
    admin_email = 'admin@mail.ru'

    developer_login = 'developer'
    developer_password = 'developer'
    developer_email = 'developer@mail.ru'

    owner_login = 'owner'
    owner_password = 'owner'
    owner_email = 'owner@mail.ru'

    def __init__(self):
        self.superuser = self.create_and_get_superuser()
        self.admin = self.create_and_get_admin()
        self.developer = self.create_and_get_developer()
        self.owner = self.create_and_get_owner()

        self.admin_group = self.create_and_get_admin_group()
        self.developer_group = self.create_and_get_developer_group()
        self.owner_group = self.create_and_get_owner_group()

        self.superuser.groups.add(self.admin_group)
        self.admin.groups.add(self.admin_group)

        self.developer.groups.add(self.developer_group)

        self.owner.groups.add(self.owner_group)

    def create_and_get_admin_group(self) -> Group:
        admins_group = Group.objects.create(name='Администраторы')
        admins_permissions = Permission.objects.all()
        admins_group.permissions.set(admins_permissions)
        return admins_group

    def create_and_get_developer_group(self) -> Group:
        developers_group = Group.objects.create(name='Разработчики')
        query = (Q(codename__contains='todo')
                 | Q(codename='view_project')
                 | Q(codename='view_user'))
        developers_permissions = Permission.objects.filter(query)
        developers_group.permissions.set(developers_permissions)
        return developers_group

    def create_and_get_owner_group(self) -> Group:
        owners_group = Group.objects.create(name='Владельцы')
        query = (Q(codename__contains='todo')
                 | Q(codename__contains='project')
                 | Q(codename='view_user'))
        owners_permissions = Permission.objects.filter(query)
        owners_group.permissions.set(owners_permissions)
        return owners_group

    def create_and_get_superuser(self) -> User:
        return User.objects.create_superuser(username=self.superuser_login,
                                             password=self.superuser_password,
                                             email=self.superuser_email)

    def create_and_get_admin(self) -> User:
        return User.objects.create_user(username=self.admin_login,
                                        password=self.admin_password,
                                        email=self.admin_email)

    def create_and_get_developer(self) -> User:
        return User.objects.create_user(username=self.developer_login,
                                        password=self.developer_password,
                                        email=self.developer_email)

    def create_and_get_owner(self) -> User:
        return User.objects.create_user(username=self.owner_login,
                                        password=self.owner_password,
                                        email=self.owner_email)

    # def create_users(self, num=100):
    #     user_login_template = 'user_{i}'
    #     user_password_template = 'password_{i}'
    #     user_email_template = f'{user_login_template}@mail.ru'

    #     number = num
    #     users = []
    #     for i in range(number):
    #         current_user_login = user_login_template.format(i=i)
    #         current_user_password = user_password_template.format(i=i)
    #         current_user_email = user_email_template.format(i=i)

    #         new_user = User(
    #             username=current_user_login,
    #             email=current_user_email,
    #             password=make_password(current_user_password, None, 'md5'),
    #             is_active=True,
    #         )
    #         users.append(new_user)
    #     return User.objects.bulk_create(users)
