from django.db import models
from django.contrib.auth import get_user_model


class TrainingProgramm(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    exercises = models.ManyToManyField(
        'training.Exercise',
        blank=True,
        verbose_name='Упражнения',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Автор тренировочной программы',
    )

    class Meta:
        verbose_name = 'Тренировачная программа'
        verbose_name_plural = 'Тренировачные программы'

    def __str__(self):
        return self.title


class Exercise(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    link = models.URLField(
        'Ссылка на демонстрацию',
        max_length=200,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.title
