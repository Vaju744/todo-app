"""
Models for the tasks app.

This module defines the database models for the tasks app, including
the Task model, which represents tasks assigned to users.
"""

from django.db import models
from django.contrib.auth import get_user_model  # Correctly fetch the User model


class Task(models.Model):
    """
    Represents a task created and assigned to a user.

    Attributes:
        user (ForeignKey): The user who owns the task.
        title (str): The title of the task.
        description (str): A detailed description of the task.
        status (str): The current status of the task.
        created_at (datetime): The timestamp when the task was created.
        updated_at (datetime): The timestamp when the task was last updated.
    """
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='tasks'
    )  # Use get_user_model() for compatibility
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='not_started'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: The title of the task.
        """
        return str(self.title)  # Explicitly convert to string
