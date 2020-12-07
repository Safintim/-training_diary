from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from api.serializers.exercise import ExerciseSerializer
from training import models


User = get_user_model()


class ExerciseViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'delete', 'put')
    permission_classes = (permissions.IsAuthenticated, )
    queryset = models.Exercise.objects.all()
    pagination_class = None
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(Q(user__is_superuser=True) | Q(user=user))
