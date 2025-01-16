from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Dynamically fetch the custom user model
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Define password explicitly for hashing and write-only usage
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user securely
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Automatically create and return an authentication token for the new user
        Token.objects.create(user=user)
        return user