from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from profiles_api import models

class UserSerializer(serializers.ModelSerializer):
    """Serializes User data"""

    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Handles creating User"""
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        user.set_password(validated_data['password'])
        # authenticated the moment user is created.
        Token.objects.create(user=user)
        
        return user

class TileSerializer(serializers.ModelSerializer):
    """Serializes Product Model"""
    
    
    def validate_status(self, value):
        """
        Check that the status field is equal to
        live, pending or archived
        """
        validation_words = ["live", "pending", "archived"]
        if not value.lower() in validation_words:
            raise serializers.ValidationError("Status must be live, pending or archived")
        return value
    
    class Meta:
        model = models.Tile
        fields = ['id', 'launch_date', 'status']

class TaskSerializer(serializers.ModelSerializer):
    """Serializes Product Model"""
    
    def validate_type(self, value):
        """
        Check that the status field contains .
        as survey, discussion, diary
        """
        validation_words = ["survey", "discussion", "diary"]
        if not value.lower() in validation_words:
            raise serializers.ValidationError("Status must be survey, discussion or diary")
        return value
    
    class Meta:
        model = models.Task
        fields = ['id', 'user', 'tile', 'title', 'order', 'type', 'description' ]
    