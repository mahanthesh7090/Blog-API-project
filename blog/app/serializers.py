from rest_framework import serializers
from .models import Posts,User,Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'username')

class CommentSerializer(serializers.ModelSerializer):
    
    
    post = serializers.PrimaryKeyRelatedField(queryset=Posts.objects.all())
    
   
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        write_only=True
    )

    
    #author = serializers.IntegerField(source='author_id', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author_id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class PostsSerializer(serializers.ModelSerializer):
    #author = UserSerializer(read_only=True)  
    
    author_id = serializers.PrimaryKeyRelatedField(
        source='author', queryset=User.objects.all(), write_only=True
    )
    
    class Meta:
        model = Posts
        fields = ('id', 'title', 'content',  'author_id', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')