from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tasks.views import task_list, create_task, welcome

class TestUrls(SimpleTestCase):
    def test_task_list_url_is_resolved(self):
        url = reverse('task_list')
        self.assertEqual(resolve(url).func, task_list)

    def test_create_task_url_is_resolved(self):
        url = reverse('create_task')
        self.assertEqual(resolve(url).func, create_task)

    def test_welcome_url_is_resolved(self):
        url = reverse('welcome')
        self.assertEqual(resolve(url).func, welcome)
