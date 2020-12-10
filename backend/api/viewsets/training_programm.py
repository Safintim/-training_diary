from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from api.serializers.training_programm import (
    TrainingProgramListSerializer,
    TrainingProgramCreateSerializer,
)
from training import models


User = get_user_model()


class TrainingProgramViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'put')
    permission_classes = (permissions.IsAuthenticated, )
    queryset = models.TrainingProgram.objects.all()
    pagination_class = None
    serializer_class = TrainingProgramListSerializer
    serializer_action_classes = {
        'list': TrainingProgramListSerializer,
        'create': TrainingProgramCreateSerializer,
        'update': TrainingProgramCreateSerializer,
    }
    # for debug
    admin = User.objects.filter(is_superuser=True).first()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user

        # for debug
        # user = self.admin
        qs = super().get_queryset()
        return qs.filter(Q(author__is_superuser=True) | Q(author=user))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        return super().update(request, args, kwargs, partial=True)
