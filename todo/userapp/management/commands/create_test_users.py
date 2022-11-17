from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


User = get_user_model()


class Command(BaseCommand):
    help = 'enter number test users'

    def add_arguments(self, parser):
        parser.add_argument('number_users', type=int)

    def handle(self, *args, **options):
        # Создадим суперпользователя
        admin_login = 'admin'
        admin_password = 'geekbrains'
        admin_email = 'geekbrains@gmail.com'

        User.objects.all().delete()

        User.objects.create_superuser(username=admin_login,
                                      password=admin_password,
                                      email=admin_email)

        user_login_template = 'user_{i}'
        user_password_template = 'password_{i}'
        user_email_template = f'{user_login_template}@mail.ru'

        number = options['number_users']

        users = []
        for i in range(number):
            current_user_login = user_login_template.format(i=i)
            current_user_password = user_password_template.format(i=i)
            current_user_email = user_email_template.format(i=i)

            new_user = User(
                username=current_user_login,
                email=current_user_email,
                password=make_password(current_user_password, None, 'md5'),
                is_active=True,
            )
            users.append(new_user)
        User.objects.bulk_create(users)
