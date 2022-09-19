from django.test import TestCase
from .models import Category, Post
from django.contrib.auth.models import User
from .models import User


class CategoryTest(TestCase):
    def test_category_creation(self):
        category_obj = Category(category_name='post category')
        self.assertEqual(str(category_obj), 'post category')


class PostTest(TestCase):

    # class PostTest(TestCase):
    def test_post_creation(self):
        user = User.objects.create_user(username='username', email='mail@gmail.com')

        category_dict = {
            "category_name": 'post category'
        }
        category = Category.objects.create(**category_dict)

        post_dict = {
            "author_name": user,
            "title": 'post title',
            "category_name": category,
            "description": 'post details',
        }
        obj = Post(**post_dict)

        # self.assertEqual(str(obj), obj.title)
        self.assertEqual(str(obj), 'post title')

    # def test_post_creation(self):
    #     user = User.objects.create_user(username='username', email='mail@gmail.com')
    #     # user.save()
    #     category = Category.objects.create(category_name='post category')
    #     # category.save()
    #     obj = Post(author_name=user, title="post title", category_name=category, description="post details")
    #     # obj.save()
    #     self.assertEqual(str(obj), 'post title')


# class PPostTest(TestCase):
#     def test_post_create(self):
#         user = User.objects.create(username='username', email='email', password='12345')
#         category_dict = {
#             'category_name': 'category name',
#         }
#         category_obj = Category(**category_dict)
#
#         post_dict = {
#             'author_name': user,
#             'title': 'post title',
#             'category_name': category_obj,
#             'description': 'post details',
#         }
#         post_obj = Post(**post_dict)
#         self.assertEqual(str(post_obj), 'post title')
