# serializers.py

from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['national_id', 'last_name', 'first_name']

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    national_id=serializers.CharField()
    password = serializers.CharField()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name','last_name','national_id', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Password must be at least 4 characters long.")
        return value

    def create(self, validated_data):
        user = UserProfile(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user