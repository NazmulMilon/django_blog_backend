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


class AllCategoryListPostTest(TestCase):  # Post is the method name of category list

    def setUp(self):
        self.valid_category = {'category_name': 'category_nme'}
        self.invalid_category = {'category_name': ''}

    def test_valid_category(self):
        response = client.post(reverse('category_list'), self.valid_category)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_category(self):
        response = client.post('category_list', self.invalid_category)
        # print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CategoryDetailAllTest(TestCase):
    def setUp(self):
        self.category_obj = Category.objects.create(category_name='category name test')
        self.category_obj2 = Category.objects.create(category_name='category name tests')
        self.valid_category_name = {
            'category_name': 'category name',
        }

    def test_valid_single_category(self):
        response = client.get(reverse('category_details', kwargs={'pk': self.category_obj.pk}))
        queryset = Category.objects.get(pk=self.category_obj.pk)
        serialize = CategorySerializer(queryset)
        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_detail_put(self):
        self.cat_obj=Category.objects.create(category_name='category name test')
        self.valid_cat_obj={
            'category_name': 'category name test',
        }
        response = client.put(reverse('category_details', kwargs={'pk': self.cat_obj.pk}),
                              self.valid_cat_obj, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryDetailPutTest(TestCase):
    def setUp(self):
        self.category_ob = Category.objects.create(category_name='category put')
        self.valid_category_name = {
            'category_name': 'category put',
        }

    def test_valid_category_put(self):
        response = client.put(reverse('category_details', kwargs={'pk': self.category_ob.pk}),
                              self.valid_category_name, content_type='application/json')
        print(response.status_code)
        print("OKKKKKKKKKKKKKKKK")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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
