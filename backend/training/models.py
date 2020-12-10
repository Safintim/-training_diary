from django.db import models
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager


class TrainingProgram(models.Model):
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
    description = models.TextField('Описание', blank=True, null=True)
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

    tags = TaggableManager()

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.title


class Training(models.Model):
    comment = models.TextField('Комментарий', blank=True, null=True)
    duration = models.CharField('Время тренировки в минутах', max_length=10)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    program = models.ForeignKey(
        TrainingProgram,
        on_delete=models.CASCADE,
        verbose_name='Программа',
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return f'{self.email} - №{self.id}'


class Set(models.Model):
    STATUS_CHOICES = (
        ('WARM_UP', 'Разминка'),
        ('EASY', 'Легко'),
        ('OK', 'Нормально'),
        ('HEAVY', 'Тяжело'),
    )
    status = models.CharField(
        'Статус',
        max_length=7,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
    )
    weight = models.PositiveIntegerField('Вес', default=0)
    reps = models.PositiveIntegerField('Количество повторений', default=0)
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        verbose_name='Упражнение',
    )
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        verbose_name='Тренировка',
    )
