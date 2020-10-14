from rest_framework import serializers

from api.serializers.exercise import (
    ExerciseSerializer,
    ExerciseCreateSerializer,
)
from training import models


class TrainingProgrammListSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = models.TrainingProgramm
        fields = ('id', 'title', 'description', 'exercises')


class TrainingProgrammCreateSerializer(serializers.ModelSerializer):
    exercises = ExerciseCreateSerializer()

    class Meta:
        model = models.TrainingProgramm
        fields = ('title', 'description', 'exercises')
