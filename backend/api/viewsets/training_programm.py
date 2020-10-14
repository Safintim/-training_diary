from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.serializers.training_programm import TrainingProgrammSerializer
from training import models


User = get_user_model()


class TrainingProgrammViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'update')
    queryset = models.TrainingProgramm.objects.all()
    serializer_class = TrainingProgrammSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user

        # for debug
        user = User.objects.filter(is_superuser=True).first()
        qs = super().get_queryset()
        return qs.filter(Q(author__is_superuser=True) | Q(author=user))
