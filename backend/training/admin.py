from django.contrib import admin
from jet.admin import CompactInline

from training import models


# TODO создать отдельную модель для м2м
class ExercisesCompactInline(CompactInline):
    model = models.TrainingProgramm.exercises.through
    extra = 0


@admin.register(models.TrainingProgramm)
class TrainProgrammAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'author',
    )

    search_fields = ('title', 'description')
    inlines = (ExercisesCompactInline, )


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'user',
    )

    search_fields = ('title', 'description')
