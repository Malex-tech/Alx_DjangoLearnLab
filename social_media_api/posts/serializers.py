from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model
from .models import Like

User = get_user_model()

class AuthorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class CommentSerializer(serializers.ModelSerializer):
    author = AuthorMiniSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author", "created_at", "updated_at"]

class PostSerializer(serializers.ModelSerializer):
    author = AuthorMiniSerializer(read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "comments_count", "created_at", "updated_at"]
        read_only_fields = ["author", "comments_count", "created_at", "updated_at"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['user', 'created_at']