from django.contrib.auth.models import User
from django.test import TestCase, Client
from ..models import Category, Post
from django.urls import reverse, resolve
from rest_framework import status
from ..serializers import PostSerializer, CategorySerializer

client = Client()


class GetAllCategoryTest(TestCase):
    def setUp(self):
        category_dict = {
            "category_name": 'category name',
        }
        Category.objects.create(**category_dict)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        queryset = Category.objects.all()
        serialize = CategorySerializer(queryset, many=True)
        # print(serialize.data)
        # print(response.data)
        # print(response.status_code)
        # print(status.HTTP_201_CREATED)
        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetAllPostTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category name',
        }
        category = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'post title',
            "author_name": user,
            "category_name": category,
            "description": 'post details',
        }
        Post.objects.create(**post_dict)

    def test_get_all_post(self):
        # self.setUp()
        # get_api_response
        response = self.client.get(reverse('post_list'))

        # get data from database
        queryset = Post.objects.all()

        serialize = PostSerializer(queryset, many=True)
        # print(response.data)
        # print(serialize.data)
        # print(response.status_code)
        # print(status.HTTP_201_CREATED)
        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
