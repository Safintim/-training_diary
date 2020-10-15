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
        exercises = validated_data.pop('exercises', [])
        instance = update_instance(instance, validated_data)

        exercises_obj = models.Exercise.objects.filter(
            id__in=[e.get('id') for e in exercises]
        )
        for obj in exercises_obj:
            exercise = get_exercise(exercises, obj.id)
            update_instance(obj, exercise)

        return instance


def get_exercise(exercises, ident):
    for e in exercises:
        if e.get('id') == ident:
            return e


def update_instance(instance, data):
    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance
