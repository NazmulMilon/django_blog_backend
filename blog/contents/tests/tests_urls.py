from django.urls import resolve, reverse
from django.test import TestCase
from ..views import PostList, PostDetail, CategoryDetail, CategoryList
from ..urls import *


class PostTest(TestCase):

    def test_post_list(self):
        print("ok")
        url = reverse('post_list')
        print(url)
        self.assertEquals(resolve(url).func.view_class, PostList)
