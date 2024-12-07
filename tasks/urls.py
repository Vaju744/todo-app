"""
URL configuration for the tasks app.

This module defines URL patterns for managing tasks and user authentication.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Base path for tasks points to task_list
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/update/', views.update_task, name='update_task'),  # Update task
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Delete task
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Edit task
]
