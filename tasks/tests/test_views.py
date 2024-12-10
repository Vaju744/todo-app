"""
Unit tests for views in the tasks app.

This module tests task-related views, including creating, updating,
and deleting tasks while ensuring user authentication.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model  # Correct import
from tasks.models import Task


class TaskViewsTest(TestCase):
    """
    Unit tests for Task views.
    """

    def setUp(self):
        """
        Set up a test user and authenticated session.
        """
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            status='not_started'
        )

    def test_create_task_view(self):
        """
        Test the create_task view for authenticated users.
        """
        response = self.client.post(reverse('create_task'), {
            'title': 'New Test Task',
            'description': 'New Test Description',
            'status': 'not_started'
        })
        self.assertEqual(response.status_code, 302)  # Expect redirect after creation
        self.assertTrue(Task.objects.filter(title='New Test Task').exists())

    def test_task_list_view(self):
        """
        Test the task_list view for logged-in users.
        """
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_delete_task_view(self):
        """
        Test deleting a task.
        """
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Expect redirect after deletion
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
