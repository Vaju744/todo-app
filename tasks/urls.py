from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     path('tasks/', views.task_list, name='task_list'),  # Task list
#     path('signup/', views.signup, name='signup'),  # Signup page
#     path('task/create/', views.create_task, name='create_task'),  # Create task
#     path('task/<int:id>/update/', views.update_task, name='update_task'),  # Update task
#     path('task/<int:id>/delete/', views.delete_task, name='delete_task'),  # Delete task
#     path('task/<int:id>/edit/', views.edit_task, name='edit_task'),  # Edit task
#     path('', views.welcome, name='welcome'),  # Welcome page
# ]

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Base path for tasks points to task_list
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_task, name='create_task'),
    path('<int:id>/update/', views.update_task, name='update_task'),  # Update task
    path('<int:id>/delete/', views.delete_task, name='delete_task'),  # Delete task
    path('<int:id>/edit/', views.edit_task, name='edit_task'),  # Edit task
]