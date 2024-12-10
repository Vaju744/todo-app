"""
Views for the tasks app.

This module contains views for managing tasks, user authentication, and task
operations like creating, editing, deleting, and listing tasks.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
#from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm


def welcome(request):
    """
    View for the welcome page.
    """
    return render(request, 'tasks/welcome.html')


def signup(request):
    """
    View for user signup.
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the login page after successful signup or
        renders the signup template with form errors.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    # Add CSS classes to form fields
    for field_name, field in form.fields.items():  # pylint: disable=unused-variable
        field.widget.attrs['class'] = 'form-control rounded-pill'

    return render(request, 'tasks/signup.html', {'form': form})


@login_required
def task_list(request):
    """
    View for listing tasks for the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the task list template.
    """
    tasks = Task.objects.filter(user=request.user)  # pylint: disable=no-member
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    """
    View for creating a new task.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the task list on success or renders the
        task form template with form errors.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def update_task(request, task_id):
    """
    View for updating an existing task.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to update.

    Returns:
        HttpResponse: Redirects to the task list on success or renders the
        task form template with form errors.
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def delete_task(request, task_id):
    """
    View for deleting an existing task.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to delete.

    Returns:
        HttpResponse: Redirects to the task list after successful deletion or
        renders the task confirm delete template.
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def edit_task(request, task_id):
    """
    View for editing an existing task.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to edit.

    Returns:
        HttpResponse: Redirects to the task list on success or renders the
        task form template with form errors.
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def custom_logout(request):
    """
    View for logging out the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the login page.
    """
    logout(request)
    return redirect('login')
