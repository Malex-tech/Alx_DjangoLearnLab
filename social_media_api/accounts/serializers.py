from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Explicitly add password field to ensure write-only input
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio', 'profile_picture']

    def validate(self, data):
        # Ensure passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Remove password2 since it's not part of the model
        validated_data.pop('password2')
        password = validated_data.pop('password')

        # Use create_user to ensure password is hashed
        user = get_user_model().objects.create_user(password=password, **validated_data)
        return user

