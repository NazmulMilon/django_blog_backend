from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['description']

