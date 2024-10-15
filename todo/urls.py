from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('new/', views.task_create, name='task-create'), #Create Url
    path('task/<int:pk>/edit/', views.task_edit, name='task-edit'),  # Edit URL
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),  # Delete URL
]
