from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/add/', views.task_create, name='task-create'),
]
