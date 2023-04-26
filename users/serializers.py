import requests
from django.contrib.auth import authenticate

from rest_framework import serializers

from users.models import Clinic,Department,Role,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'uuid', 'email', 'name', 'staff_id','clinic',
            'department','role','phone','birthday','zodiac',
            'staff_code','is_staff','resigned_at','nickname','trail_till',
            'password_set','is_active'
        )

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        data['username'] = data['username'].lower()
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to login with provided credentials."
        )