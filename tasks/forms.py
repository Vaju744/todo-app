"""
Forms for the tasks app.

This module defines forms for creating and updating tasks.
It primarily includes the TaskForm, which maps directly to the Task model.
"""

from django import forms
from .models import Task


# Pylint warning disabled because this class is a minimal Django ModelForm.
# pylint: disable=too-few-public-methods
class TaskForm(forms.ModelForm):
    """
    A form for creating and updating Task instances.

    This form provides fields for the title, description, and status.
    The status field uses a dropdown widget with predefined choices.
    """

    class Meta:
        """Meta class defining model and fields."""
        model = Task
        fields = ['title', 'description', 'status']
        widgets = {
            'status': forms.Select(choices=Task.STATUS_CHOICES),
        }
