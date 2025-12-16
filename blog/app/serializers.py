from rest_framework import serializers
from .models import Posts,User,Comment
from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'username')
    


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

class CommentContentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Comment
        fields = ('content',)
    
class CommentSerializer(serializers.ModelSerializer):
    
    
    post = serializers.PrimaryKeyRelatedField(queryset=Posts.objects.all())
    author = serializers.PrimaryKeyRelatedField(read_only=True)
      
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author','created_at', 'updated_at')
    def validate_content(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Comment is too short")
        return value
    
class PostsSerializer(serializers.ModelSerializer):
    #author = UserSerializer(read_only=True)  
    comments = CommentContentSerializer(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Posts
        fields = ("id", "title", "content","comments", "author", "created_at", "updated_at")
        read_only_fields = ("id", "author", "created_at", "updated_at")

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty")
        return value