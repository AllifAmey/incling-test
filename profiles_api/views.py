from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import authentication
from django.contrib.auth.models import User

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

    
class TileViewset(viewsets.ModelViewSet):
    """Viewset to create,update and delete Tile models """
    serializer_class = serializers.TileSerializer
    queryset = models.Tile.objects.all() 
    authentication_classes = [authentication.TokenAuthentication]
    
    
    def list(self, request):
        """List all of the tiles and their associated tasks"""
        
        all_tiles = models.Tile.objects.all()
        tiles_list = []
        for tile in all_tiles:
            tasks_in_tile = models.Task.objects.filter(tile=tile)
            serializer = serializers.TileSerializer(tile)
            if len(tasks_in_tile) == 0:
                tiles_list.append({"tile": serializer.data , "tasks": "Empty"})
            else:
                #
                tasks_serialized = serializers.TaskSerializer(tasks_in_tile,many=True)
                tiles_list.append({"tile": serializer.data , "tasks": tasks_serialized.data})
        return Response(tiles_list, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        """Retrieve Tile and display all the individual tasks associated with it."""
        
        tile = models.Tile.objects.get(id=pk)
        serializer_tile = self.serializer_class(tile)
        tasks_in_tile =  models.Task.objects.filter(tile=tile)
        serializer_task = serializers.TaskSerializer(tasks_in_tile, many=True)
        response = {"tile": serializer_tile.data, "tasks": serializer_task.data}
        
        return Response(response, status=status.HTTP_200_OK)


class TaskViewset(viewsets.ModelViewSet):
    """Only Users can create task objects and view their own tasks"""

    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all() 
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.UpdateOwnObj,]
    
    def list(self, request):
        """User can only see their own tasks"""
        user = request.user
        tasks = models.Task.objects.filter(user=user)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Users can create their own task"""
        user = request.user
        request_user = request.data["user"]
        if user.id != request_user:
            return Response({"message": "You can not edit other user's tasks"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and retrieving profiles"""
    
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    http_method_names = ["get", "post"]
    

