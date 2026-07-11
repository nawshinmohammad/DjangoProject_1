from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['owner']
        fields = ['task_title', 'description', 'due_date', 'status']


        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"})
        }

        