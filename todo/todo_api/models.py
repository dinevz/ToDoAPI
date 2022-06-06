from django.db import models

# Create your models here.
PRIORITY_CHOICES = (
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low")
)

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, blank=True)
    priority = models.CharField(max_length=20, choices= PRIORITY_CHOICES, default= 'Low')
    
    def __str__(self):
        return self.task

    