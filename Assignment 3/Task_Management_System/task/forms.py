from django import forms
from .models import TaskModel
from django.forms.widgets import NumberInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ('__all__')
        widgets = {
            'task_assign_date' : NumberInput(attrs={'type': 'date'}),
            'categories': forms.CheckboxSelectMultiple(),
        }