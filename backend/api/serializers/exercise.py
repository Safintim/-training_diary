from rest_framework import serializers

from training import models


class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = models.Exercise
        fields = ('id', 'title')
