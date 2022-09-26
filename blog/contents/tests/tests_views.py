from django.contrib.auth.models import User
from django.test import TestCase, Client
from ..models import Category, Post, Comment, Reply
from django.urls import reverse, resolve
from rest_framework import status
from ..serializers import PostSerializer, CategorySerializer, CommentSerializer, ReplySerializer
import json
from rest_framework.response import Response

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

    def test_category_list_post(self):
        response = client.post(reverse('category_list'), self.valid_category)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


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
        # self.cat_obj=Category.objects.create(category_name='category name test')
        # self.valid_cat_obj={
        #     'category_name': 'category name test',
        # }
        response = client.put(reverse('category_details', kwargs={'pk': self.category_obj.pk}),
                              self.valid_category_name, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category_detail(self):
        response = client.delete(reverse('category_details', kwargs={'pk': self.category_obj.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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

    def test_valid_delete_category(self):
        response = client.delete(reverse('category_details', kwargs={'pk': self.category_ob.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GetAllPostTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category name',
        }
        category = Category.objects.create(**category_dict)

        self.post_dict = {
            "title": 'post title',
            "author_name": user.id,
            "category_name": category.id,
            "description": 'post details',
        }
        # Post.objects.create(**post_dict)

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

    def test_post_list_post(self):
        response = client.post(reverse('post_list'), self.post_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PostDetailsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='username')
        category_name = Category.objects.create(category_name='category name')

        self.post_queryset = Post.objects.create(title='title test name', author_name=user,
                                                 category_name=category_name,
                                                 description='post details')
        self.valid_post_details = {
            'title': 'title test',
            'author_name': user.id,
            'category_name': category_name.id,
            'description': 'post details',
        }

    def test_get_single_post_detail(self):
        response = client.get(reverse('post_detail', kwargs={'pk': self.post_queryset.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_single_post_detail(self):
        response = client.put(reverse('post_detail', kwargs={'pk': self.post_queryset.pk}),
                              self.valid_post_details,
                              content_type='application/json')
        # print(" everything is ok")
        # print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_post_detail(self):
        response = client.delete(reverse('post_detail', kwargs={'pk': self.post_queryset.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_something(self):
    #     response = client.put(reverse('post_detail', kwargs={'pk': self.post_queryset.pk}),
    #                           data=json.dumps(self.valid_post_details))

    def test_put_post_details(self):
        response = client.put(reverse('post_detail', kwargs={'pk': self.post_queryset.pk}),
                              self.valid_post_details,
                              content_type='application/json')
        # print("another practice")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post_details(self):
        response = client.delete(reverse('post_detail', kwargs={'pk': self.post_queryset.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GetALLCommentListTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category name',
        }
        category_queryset = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'title test',
            "author_name": user,
            "category_name": category_queryset,
            "description": 'post details',

        }
        post_queryset = Post.objects.create(**post_dict)

        self.comment_dict = {
            "posts": post_queryset.id,
            "comment_detail": 'description test',
            "commenter": user.id,
        }
        # Comment.objects.create(**comment_dict)

    def test_comment_list_get(self):
        response = self.client.get(reverse('comment_list'))
        queryset = Comment.objects.all()
        serialize = CommentSerializer(queryset, many=True)
        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_list_post(self):
        response = client.post(reverse('comment_list'), self.comment_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentDetailsTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', email='m@gmail.com')
        category_queryset = Category.objects.create(category_name='category name')
        post_queryset = Post.objects.create(title='title test', author_name=user, category_name=category_queryset,
                                            description='post details test')
        self.comment_queryset = Comment.objects.create(posts=post_queryset, comment_detail='comment details test',
                                                       commenter=user)
        self.comment_dict = {
            "posts": post_queryset.id,
            "comment_detail": 'comment description test',
            "commenter": user.id,
        }

        # comment_queryset = Comment.objects.create(**comment_dict)

    def test_single_comment_detail(self):
        response = client.get(reverse('comment_detail', kwargs={'pk': self.comment_queryset.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_comment_details(self):
        response = client.put(reverse('comment_detail', kwargs={'pk': self.comment_queryset.pk}),
                              self.comment_dict,
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment_details(self):
        response = client.delete(reverse('comment_detail', kwargs={'pk': self.comment_queryset.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReplyListTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='user name', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category name',
        }
        category_queryset = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'title test',
            "author_name": user,
            "category_name": category_queryset,
            "description": 'write details test',
        }
        post_queryset = Post.objects.create(**post_dict)

        comment_dict = {
            "posts": post_queryset,
            "comment_detail": 'comment description',
            "commenter": user,
        }
        comment_queryset = Comment.objects.create(**comment_dict)

        self.reply_queryset = {
            "comment": comment_queryset.id,
            "reply_detail": 'reply description',
            "replier": user.id,
        }

    def test_reply_get_list(self):
        response = client.get(reverse('reply_list'))
        queryset = Reply.objects.all()
        serialize = ReplySerializer(queryset, many=True)
        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reply_post_list(self):
        response = client.post(reverse('reply_list'), self.reply_queryset)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReplyDetailTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', email='m@gmail.com', password='12345')
        category_dict = {
            "category_name": 'category_name',
        }
        category_queryset = Category.objects.create(**category_dict)

        post_dict = {
            "title": 'title test',
            "author_name": user,
            "category_name": category_queryset,
            "description": 'post details',
        }
        post_queryset = Post.objects.create(**post_dict)

        comment_dict = {
            "posts": post_queryset,
            "comment_detail": 'comment detail test',
            "commenter": user,
        }
        comment_queryset = Comment.objects.create(**comment_dict)

        self.reply_queryset = Reply.objects.create(comment=comment_queryset, reply_detail='reply details test',
                                                   replier=user)
        self.reply_dict = {
            "comment": comment_queryset.id,
            "reply_detail": 'reply details test',
            "replier": user.id,

        }

    def test_reply_detail_get(self):
        response = client.get(reverse('reply_detail', kwargs={'pk': self.reply_queryset.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
