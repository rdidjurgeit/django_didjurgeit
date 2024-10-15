from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    created = models.DateTimeField(auto_now_add=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started'
        )
    
    #other fields 
    def __str__(self):
        return self.title  # This will display the title instead of 'Task object'