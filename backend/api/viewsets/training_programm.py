from django.db.models import Q
from rest_framework import viewsets

from api.serializers.training_programm import TrainingProgrammSerializer
from training import models


class TrainingProgrammViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'update')
    queryset = models.TrainingProgramm.objects.all()
    serializer_class = TrainingProgrammSerializer

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(Q(author__is_superuser=True) | Q(author=user))
