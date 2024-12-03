from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:id>/update/', views.update_task, name='update_task'),
    path('task/<int:id>/delete/', views.delete_task, name='delete_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),  # Edit task
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('create/', views.create_task, name='create_task'),
]
