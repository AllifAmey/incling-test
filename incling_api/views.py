from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import authentication
from django.contrib.auth.models import User

from incling_api import models
from incling_api import serializers
from incling_api import permissions

    
class TileViewset(viewsets.ModelViewSet):
    """Viewset to create,update and delete Tile models """
    serializer_class = serializers.TileSerializer
    queryset = models.Tile.objects.all() 

    
    


class TaskViewset(viewsets.ModelViewSet):
    """Only Users can create task objects and view their own tasks"""

    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all() 
    
   
    
    
        

    

