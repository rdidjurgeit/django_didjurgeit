from django.db import models
from django.contrib.auth.models import User  # Import the User model


class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    created = models.DateTimeField(auto_now_add=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #other fields 
    def __str__(self):
        return self.title  # This will display the title instead of 'Task object'