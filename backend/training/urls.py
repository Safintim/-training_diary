from django.urls import path

from training import views

urlpatterns = (
    path('training-programs/', views.TrainingProgramListView.as_view(), name='training-program-list'),
    path('training-programs/<int:pk>/', views.TrainingProgramDetailView.as_view(), name='training-program-detail'),
    path('training-programms/create/', views.CreateTrainingProgramView.as_view(), name='training-program-add'),
)
