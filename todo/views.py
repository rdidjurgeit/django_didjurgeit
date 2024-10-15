from django.shortcuts import render
from django.views import generic

from .models import Task

class TaskList(generic.ListView):
    model = Task