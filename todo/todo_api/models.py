from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.task

    