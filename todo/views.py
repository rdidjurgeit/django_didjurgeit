from django.shortcuts import render, redirect
from django.views import generic

from .models import Task
from .forms import TaskForm

class TaskList(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'  # Specify your template name if needed
    
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