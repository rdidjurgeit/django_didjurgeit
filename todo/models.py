from django.db import models

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField()