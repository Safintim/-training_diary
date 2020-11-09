from django.db import models
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.CharField('Описание', max_length=200)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
