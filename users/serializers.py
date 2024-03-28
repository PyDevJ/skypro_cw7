from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User Model."""
    class Meta:
        model = User
        fields = '__all__'
