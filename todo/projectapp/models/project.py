from django.db import models
from django.conf import settings

user_model_name: str = settings.AUTH_USER_MODEL


class Project(models.Model):
    """Проект, для которого записаны TODO

    """
    title = models.CharField(
        verbose_name='Название проекта',
        max_length=255,
        db_index=True,
        help_text='Название проекта длинной до 255 символов',
        unique=True
    )
    url_repo = models.URLField(
        verbose_name='Ссылка на репозиторий',
        max_length=200,
        help_text='Сылка не репозиторий длинной до 200 символов',
        unique=True,
        null=True,
        blank=True,
    )
    users = models.ManyToManyField(
        verbose_name='Работники на проекте',
        to=user_model_name,
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
