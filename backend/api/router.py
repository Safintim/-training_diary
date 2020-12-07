from rest_framework.routers import DefaultRouter

from api.viewsets.training_programm import TrainingProgrammViewSet
from api.viewsets.exercise import ExerciseViewSet


router = DefaultRouter()
router.register(
    'training_programms',
    TrainingProgrammViewSet,
    basename='training_programms',
)
router.register(
    'exercises',
    ExerciseViewSet,
    basename='exercises',
)
