from django.contrib import admin
from jet.admin import CompactInline

from training import models


@admin.register(models.TrainingProgramm)
class TrainProgrammAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'author',
    )

    search_fields = ('title', 'description')


@admin.register(models.Exercise)
class ExercisesAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'user',
    )

    search_fields = ('title', 'description')
