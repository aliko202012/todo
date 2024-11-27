from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']

    def validate_phone_number(self, value):
        if not value.startswith('+996') or len(value) != 13:
            raise serializers.ValidationError("+996********")
        return value
