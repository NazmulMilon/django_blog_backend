from rest_framework import serializers
from .models import Post, Category, Comment, Reply


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['created_at', 'updated_at']
        # fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']
        # fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']
        # fields = '__all__'

        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        exclude = ['created_at', 'updated_at']
        # fields = '__all__'
