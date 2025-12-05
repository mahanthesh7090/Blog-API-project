from rest_framework import serializers
from .models import Posts,User,Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        read_only_fields = ('id', 'date_joined')

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields="__all__"
        read_only_fields = ('created_at', 'updated_at')

class PostsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Posts
        fields="__all__"
        read_only_fields = ('created_at', 'updated_at')