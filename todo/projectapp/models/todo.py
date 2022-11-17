from django.db import models
from django.conf import settings

user_model_name: str = settings.AUTH_USER_MODEL


class Todo(models.Model):
    """Заметки

    """
    project = models.ForeignKey(
        verbose_name='Проект',
        to='projectapp.Project',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст заметки',
        help_text='Текст заметки'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
        db_index=True

    )
    updated_at = models.DateTimeField(
        verbose_name='Дата и время редактирования',
        auto_now=True,
        db_index=True
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=user_model_name,
        on_delete=models.CASCADE,

    )
    is_active = models.BooleanField(
        verbose_name='Запись активна',
        default=False,
    )

    def __str__(self):
        edge = 30
        text_ = (self.text[0:edge]
                 if len(self.text) < edge
                 else f'{self.text[0:edge]}...')
        return text_

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
