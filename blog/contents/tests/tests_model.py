# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Category, Post, Comment, Reply


class TestCategory(TestCase):
    def test_create_category(self):
        category_dict = {
            "category_name": 'category name',
        }
        obj = Category(**category_dict)
        self.assertEquals(str(obj), 'category name')


class TestPost(TestCase):
    def test_post_create(self):
        user = User.objects.create(username='username', email='m@gmail.com')
        category_dict = {
            "category_name": 'category name',
        }
        category_obj = Category.objects.create(**category_dict)

        post_dict = {
            "author_name": user,
            "title": 'post title',
            "category_name": category_obj,
            "description": 'post details',
        }
        post_obj = Post(**post_dict)
        self.assertEquals(str(post_obj), 'post title')


class TestComment(TestCase):
    def test_comment_create(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category name',
        }
        category_queryset = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'post title test',
            "author_name": user,
            "category_name": category_queryset,
            "description": 'description test',
        }
        post_queryset = Post.objects.create(**post_dict)

        comment_dict = {
            "posts": post_queryset,
            "comment_detail": 'comment detail test',
            "commenter": user,
        }

        comment_queryset = Comment(**comment_dict)
        self.assertEquals(str(comment_queryset), 'comment detail test')


class TestReply(TestCase):
    def test_reply_create(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category_name',
        }
        category_queryset = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'write title of post',
            "author_name": user,
            "category_name": category_queryset,
            "description": 'details test',

        }
        post_queryset = Post.objects.create(**post_dict)

        comment_dict = {
            "posts": post_queryset,
            "comment_detail": 'comment description',
            "commenter": user,
        }

        comment_queryset = Comment.objects.create(**comment_dict)

        reply_dict = {
            "comment": comment_queryset,
            "reply_detail": 'description of a reply',
            "replier": user,
        }

        reply_queryset = Reply(**reply_dict)
        self.assertEquals(str(reply_queryset), 'description of a reply')

'''Old method to test django models'''
#
#
# class CategoryTest(TestCase):
#     def create_category(self, category_name="Only test category name"):
#         return Category.objects.create(category_name=category_name)
#
#     def test_category_creation(self):
#         category_obj = self.create_category()
#         self.assertTrue(isinstance(category_obj, Category))
#         self.assertEqual(category_obj.category_name, category_obj.category_name)
#
#     # class PostTest(TestCase):
#     def test_post_creation(self):
#         user = User.objects.create_user(username='username', email='mail@gmail.com')
#         # user.save()
#         category = Category.objects.create(category_name='post category')
#         # category.save()
#         obj = Post(author_name=user, title="post title", category_name=category, description="post details")
#         # obj.save()
#         self.assertEqual(str(obj), 'post title')
#
#
#
#

# class TestModel(TestCase):
#
#     def test_should_create_user(self):
#         user = User.objects.create_user(username='username', email='m@gmail.com')
#         # user.set_password('12345')
#         # user.save()
#         todo = Todo(owner=user, title="Buy milk", description='get it done')
#         todo.save()
#         self.assertEqual(str(todo), 'Buy milk')
#
