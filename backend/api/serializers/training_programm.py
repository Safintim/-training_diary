from rest_framework import serializers

from api.serializers.exercise import ExerciseSerializer
from training import models


class TrainingProgrammSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = models.TrainingProgramm
        fields = ('id', 'title', 'description', 'exercises')
