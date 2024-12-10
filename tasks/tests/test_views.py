"""
Unit tests for task_list view in the tasks app.

This module contains tests for the task_list view,
including access control, response status, and template usage.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task


class TaskListViewTest(TestCase):
    """
    Tests for the task_list view in the tasks app.
    """

    def setUp(self):
        """
        Set up a test user and a sample task for testing the task list view.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(  # pylint: disable=no-member
            title='Test Task', user=self.user
        )

    def test_redirect_if_not_logged_in(self):
        """
        Test that the task list view redirects unauthenticated users to the login page.
        """
        response = self.client.get(reverse('task_list'))
        self.assertRedirects(response, '/login/?next=/tasks/')

    def test_logged_in_user_sees_tasks(self):
        """
        Test that a logged-in user sees tasks in the task list view.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_list.html')
