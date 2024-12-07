"""
Unit tests for URL patterns in the tasks app.

This module tests that URL patterns resolve to the correct views,
ensuring the application's routing works as expected.
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tasks.views import task_list, create_task, welcome


class TestUrls(SimpleTestCase):
    """
    Unit tests for URL resolution in the tasks app.
    """

    def test_task_list_url_is_resolved(self):
        """
        Test that the task list URL resolves to the task_list view.
        """
        url = reverse('task_list')
        self.assertEqual(resolve(url).func, task_list)

    def test_create_task_url_is_resolved(self):
        """
        Test that the create task URL resolves to the create_task view.
        """
        url = reverse('create_task')
        self.assertEqual(resolve(url).func, create_task)

    def test_welcome_url_is_resolved(self):
        """
        Test that the welcome URL resolves to the welcome view.
        """
        url = reverse('welcome')
        self.assertEqual(resolve(url).func, welcome)
