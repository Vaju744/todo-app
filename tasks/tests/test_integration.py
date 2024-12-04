from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task

class TaskIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_task_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_task'), {
            'title': 'Integration Test Task',
            'description': 'Integration Test Description',
            'completed': False
        })
        self.assertEqual(response.status_code, 302) 
