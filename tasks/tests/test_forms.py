"""
Unit tests for TaskForm in the tasks app.

This module contains unit tests that validate the behavior of TaskForm,
ensuring proper form validation and required fields.
"""

from django.test import TestCase
from tasks.forms import TaskForm


class TaskFormTest(TestCase):
    """
    Unit tests for TaskForm validation.
    """

    def test_task_form_valid(self):
        """
        Test TaskForm with valid data.

        Ensures the form is valid when all required fields are provided.
        """
        form = TaskForm(data={
            'title': 'New Task',
            'description': 'Task Description',
            'status': 'not_started'  # Corrected the field name
        })
        print(form.errors)  # Add this for debugging if needed
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        """
        Test TaskForm with missing required fields.

        Ensures the form is invalid when required fields are missing.
        """
        form = TaskForm(data={})  # Missing all required fields
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
