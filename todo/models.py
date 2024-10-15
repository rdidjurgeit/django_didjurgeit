from django.db import models

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    #other fields 
    def __str__(self):
        return self.title  # This will display the title instead of 'Task object'