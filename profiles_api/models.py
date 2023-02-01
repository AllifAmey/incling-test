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
         return f'Tile created at {self.launch_date}'
    
class Task(models.Model):
    """Task object representing single task each user completes"""
    
    tile = models.ForeignKey(
        Tile,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)
    title = models.CharField(max_length=255)
    order = models.TextField()
    description = models.TextField()
    type = models.CharField(max_length=255)
    
    
    def __str__(self):
         """Return the model as a string"""
         return f'{self.user}\'s task with title {self.title}'