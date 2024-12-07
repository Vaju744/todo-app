"""
Unit tests for the Task model in the tasks app.

This module tests the functionality and behavior of the Task model,
including creation, field values, and string representation.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task


class TaskModelTest(TestCase):
    """
    Unit tests for the Task model.
    """

    def setUp(self):
        """
        Set up a test user and a test task for use in the tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(  # pylint: disable=no-member
            title='Test Task',
            description='Test Description',
            status='not_started',
            user=self.user
        )

    def test_task_creation(self):
        """
        Test that a Task instance is created with the correct field values.
        """
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.status, 'not_started')
        self.assertEqual(self.task.user, self.user)

    def test_string_representation(self):
        """
        Test the string representation of the Task model.
        """
        self.assertEqual(str(self.task), 'Test Task')
