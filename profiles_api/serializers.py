from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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

    