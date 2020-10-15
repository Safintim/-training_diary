from rest_framework import serializers

from api.serializers.exercise import ExerciseSerializer
from training import models


class TrainingProgrammListSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = models.TrainingProgramm
        fields = ('id', 'title', 'description', 'exercises')


class TrainingProgrammCreateSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = models.TrainingProgramm
        fields = ('title', 'description', 'exercises')

    def create(self, validated_data):
        user = self.context['request'].user
        exercises = validated_data.pop('exercises', [])
        training = models.TrainingProgramm.objects.create(**validated_data)
        exercise_objs = [
            models.Exercise.objects.create(**exercise, user=user)
            for exercise in exercises
        ]
        training.exercises.add(*exercise_objs)
        return training

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        # TODO добавить обновление
        # validated_data.pop(exercises, [])
        # for attr, value in validated_data.items():
