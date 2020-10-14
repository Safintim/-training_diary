from rest_framework import serializers

from training import models


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ('id', 'title')


class ExerciseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ('title', )
