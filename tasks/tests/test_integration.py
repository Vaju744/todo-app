"""
Integration tests for the tasks app.

This module tests the integration of views, models, and forms
for creating tasks in the tasks app.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task


class TaskIntegrationTest(TestCase):
    """
    Integration tests for the Task app.
    """

    def setUp(self):
        """
        Set up a test user for authentication.
        """
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )

    def test_create_task_view(self):
        """
        Test the create_task view for authenticated users.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_task'),
            {
                'title': 'Integration Test Task',
                'description': 'Integration Test Description',
                'status': 'not_started',  # Corrected field name
            },
        )
        self.assertEqual(response.status_code, 302)  # Expect redirect after successful creation

        # Verify that the task was created
        task = Task.objects.get(title='Integration Test Task')  # pylint: disable=no-member
        self.assertEqual(task.description, 'Integration Test Description')
        self.assertEqual(task.status, 'not_started')
        self.assertEqual(task.user, self.user)
