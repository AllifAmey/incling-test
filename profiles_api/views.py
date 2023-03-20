from rest_framework import viewsets

from django.contrib.auth.models import User

from profiles_api import serializers



class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and retrieving profiles"""
    
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    http_method_names = ["get", "post"]
    

