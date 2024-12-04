from django.test import TestCase
from tasks.forms import TaskForm

class TaskFormTest(TestCase):
    def test_task_form_valid(self):
        form = TaskForm(data={
            'title': 'New Task',
            'description': 'Task Description',
            'completed': False
        })
        print(form.errors)  # Add this to check why the form is invalid
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
