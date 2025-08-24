from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)
    following = UserMiniSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "bio", "profile_picture",
                  "followers_count", "following_count", "following"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # <-- now matches the check
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
