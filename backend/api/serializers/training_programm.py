from rest_framework import serializers

from training import models


class TrainingProgrammSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrainingProgramm
        fields = ('title', 'description', 'exercises')
