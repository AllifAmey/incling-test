from rest_framework import serializers

from incling_api import models

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
        fields = ['id', 'tile', 'title', 'order', 'type', 'description' ]