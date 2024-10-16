from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('new/', views.task_create, name='task-create'), #Create Url
    path('task/<int:pk>/edit/', views.task_edit, name='task-edit'),  # Edit URL
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),  # Delete URL
    path('task/<int:pk>/toggle_status/', views.task_toggle_status, name='task-toggle-status'), #Toggling Status
    
    # Authentication URLs
    path('register/', views.register, name='register'),  # User registration URL
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]
