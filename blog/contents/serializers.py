from rest_framework import serializers
from .models import Post, Category, Comment, Reply


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        
class ReplySerializers(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
