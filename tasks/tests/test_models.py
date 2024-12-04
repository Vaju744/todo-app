from django.test import TestCase
from tasks.models import Task
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            completed=False,
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user, self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.task), 'Test Task')
