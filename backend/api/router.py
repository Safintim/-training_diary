from rest_framework.routers import DefaultRouter

from api.viewsets.training_programm import TrainingProgrammViewSet


router = DefaultRouter()
router.register(
    'training_programms',
    TrainingProgrammViewSet,
    basename='training_programms',
)
