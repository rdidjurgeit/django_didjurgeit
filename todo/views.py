from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views import View
from .models import Task
from .forms import TaskForm


# Other views
@method_decorator(login_required, name='dispatch')
class TaskList(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'  # Specify your template name if needed
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)  # Show only the tasks created by the logged-in user

#Task Create Stage
    
@login_required
def task_create(request):
    if request.method == 'POST':  # Check if the form has been submitted
        form = TaskForm(request.POST)  # Bind the form to the submitted data
        if form.is_valid():  # Validate the form
            task = form.save(commit=False)  # Create a task object but don't save it yet
            task.user = request.user  # Assign the task to the logged-in user
            task.save()  # Now save the task
            return redirect('task-list')  # Redirect to the task list after saving
    else:
        form = TaskForm()  # Create a new blank form for GET requests

    context = {
        "form": form,
    }
    return render(request, "todo/task_create.html", context)

#Task Edit

@login_required
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

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('task-list')  # Redirect to task list
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

# Task Toggle Status

@login_required
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
