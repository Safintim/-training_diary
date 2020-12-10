from django.db.models import Q
from django.views import generic

from account.models import User
from training import models


class TrainingProgramListView(generic.ListView):
    model = models.TrainingProgram
    context_object_name = 'programs'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = User.objects.filter(is_superuser=True).first()
        qs = super().get_queryset()
        return qs.filter(Q(author__is_superuser=True) | Q(author=user))


class TrainingProgramDetailView(generic.DetailView):
    model = models.TrainingProgram
    context_object_name = 'program'

class CreateTrainingProgramView(generic.CreateView):
    model = models.TrainingProgram
    fields = ('title', 'description', 'image', 'exercises')