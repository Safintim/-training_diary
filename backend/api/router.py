from rest_framework.routers import DefaultRouter

from api.viewsets.training_programm import TrainingProgramViewSet
from api.viewsets.exercise import ExerciseViewSet


router = DefaultRouter()
router.register(
    'training_programs',
    TrainingProgramViewSet,
    basename='training_programs',
)
router.register(
    'exercises',
    ExerciseViewSet,
    basename='exercises',
)
