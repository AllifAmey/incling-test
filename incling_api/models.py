from django.db import models
from django.conf import settings

# Create your models here.
class Tile(models.Model):
    """Tile container"""
    
    #I assume tasks can have different launch dates.
    # auto_now=True is thus not used.
    launch_date = models.DateField(
        
    )
    status = models.CharField(max_length=255)
    
    def __str__(self):
         """Return the model as a string"""
         return f'Tile created at {self.launch_date} with status {self.status}'
    
class Task(models.Model):
    """Task object"""
    
    tile = models.ForeignKey(
        Tile,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    order = models.TextField()
    description = models.TextField()
    type = models.CharField(max_length=255)
    
    
    def __str__(self):
         """Return the model as a string"""
         return f'Task with title: {self.title}'