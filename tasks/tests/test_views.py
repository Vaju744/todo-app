from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task

class TaskListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(title='Test Task', user=self.user)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('task_list'))
        self.assertRedirects(response, '/login/?next=/tasks/')

    def test_logged_in_user_sees_tasks(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_list.html')
