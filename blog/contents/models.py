from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, help_text='type of post category')
    created_at = models.DateTimeField(auto_now_add=True, help_text='category added date')
    updated_at = models.DateTimeField(auto_now=True, help_text='category updated date')

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='blog post title name')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, help_text='blogs writer name')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='foreignkey relationship with '
                                                                                    'Category')
    description = models.TextField(help_text='body of a single blog post')
    created_at = models.DateTimeField(auto_now_add=True, help_text='blog written date')
    updated_at = models.DateTimeField(auto_now=True, help_text='last update time')

    def __str__(self):
        return self.title


class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, help_text='post details')
    comment_detail = models.CharField(max_length=200, help_text='comment body')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, help_text='person who comment')
    created_at = models.DateTimeField(auto_now_add=True, help_text='comment written time')
    updated_at = models.DateTimeField(auto_now=True, help_text='comment updated time')

    def __str__(self):
        return self.comment_detail
#
# class Todo(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     is_completed = models.BooleanField(default=False)
#     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
