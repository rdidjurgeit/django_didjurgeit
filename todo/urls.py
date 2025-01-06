from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('new/', views.task_create, name='task-create'),
    path(
        'task/<int:pk>/edit/',
        views.task_edit,
        name='task-edit'
    ),
    path(
        'task/<int:pk>/delete/',
        views.task_delete,
        name='task-delete'
    ),
    path(
        'task/<int:pk>/toggle_status/',
        views.task_toggle_status,
        name='task-toggle-status'
    ),
    path('membership/', views.premium_membership, name='premium-membership'),
    path('register/', views.register, name='register'),
]
