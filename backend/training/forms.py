from django import forms

from training import models


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = ('title', )


ExerciseFormSet = forms.modelformset_factory(
    models.Exercise,
    fields=('title', ),
    widgets={
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название',
        }),
    }
)


class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = models.TrainingProgram
        fields = ('title', 'description', 'image', 'exercises')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'exercises': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'multiple': 'True',
                'size': 10,
            }),
        }
