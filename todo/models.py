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
    due_date = models.DateField(null=True, blank=True)  # Add due_date field (optional)
    #other fields 
    
    def __str__(self):
        return self.title  # This will display the title instead of 'Task object'
    
class PremiumMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membership')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Premium Membership for {self.user.username} - {'Active' if self.is_active else 'Inactive'}"
