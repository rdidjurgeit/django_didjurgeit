from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views import View
from .models import Task
from .forms import TaskForm

# Other views

class TaskList(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'  # Specify your template name if needed

#Task Create Stage    

def task_create(request):
    if request.method == 'POST':  # Check if the form has been submitted
        form = TaskForm(request.POST)  # Bind the form to the submitted data
        if form.is_valid():  # Validate the form
            form.save()  # Save the new task
            return redirect('task-list')  # Redirect to the task list after saving
    else:
        form = TaskForm()  # Create a new blank form for GET requests

    context = {
        "form": form,
    }
    return render(request, "todo/task_create.html", context)

#Task Edit

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Get the task or return a 404 if not found
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind the form to the existing task
        if form.is_valid():
            form.save()  # Save changes to the task
            return redirect('task-list')  # Redirect to task list
    else:
        form = TaskForm(instance=task)  # Populate the form with existing task data

    context = {
        'form': form,
    }
    return render(request, 'todo/task_edit.html', context)

#Task Delete

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('task-list')  # Redirect to task list
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

# Task Toggle Status

def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Toggle between the statuses
    if task.status == 'not_started':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'completed'
    else:
        task.status = 'not_started'

    task.save()  # Save the new status
    return redirect('task-list')
