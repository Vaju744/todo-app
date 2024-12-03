from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from django.contrib.auth import logout

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'tasks/signup.html', {'form': form})
from django import forms

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    
    # Add CSS classes to form fields
    for field_name, field in form.fields.items():
        field.widget.attrs['class'] = 'form-control rounded-pill'

    return render(request, 'tasks/signup.html', {'form': form})

    
    # Add classes to form fields
    for field_name, field in form.fields.items():
        field.widget.attrs['class'] = 'form-control rounded-pill'

    return render(request, 'tasks/signup.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/task_form.html', {'form': form})

# @login_required
# def create_task(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)  # Do not save yet
#             task.user = request.user       # Associate the task with the logged-in user
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associate task with logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})



@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def custom_logout(request):
    logout(request)
    return redirect('login')

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def edit_task(request, pk):
    # Fetch the specific task that belongs to the logged-in user
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        # Populate the form with POST data and bind it to the existing task
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect back to the task list
    else:
        # Initialize the form with the existing task data
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
