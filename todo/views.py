from django.shortcuts import render
from django.views import generic

from .models import Task
from .forms import TaskForm

class TaskList(generic.ListView):
    model = Task
    
def task_create(request):
    form = TaskForm()
    context = {
        "form": form,
    }
    return render(
        request,
        "todo/task_create.html",
        context
    )