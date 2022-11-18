from django.contrib import admin
from .models import Category, Post, Comment, Reply


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'category_name', 'description', 'created_at', 'updated_at']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['posts', 'comment_detail', 'commenter', 'created_at', 'updated_at']


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'reply_detail', 'replier', 'created_at', 'updated_at']


admin.site.register(Reply, ReplyAdmin)
