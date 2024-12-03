# from django.db import models
# from django.contrib.auth.models import User

# class Task(models.Model):
#     STATUS_CHOICES = [
#         ('not_started', 'Not yet started'),
#         ('in_progress', 'In progress'),
#         ('completed', 'Completed'),
#     ]
    
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='not_started',
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Link task to user
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

