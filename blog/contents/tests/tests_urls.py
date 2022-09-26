from django.test import TestCase
from django.urls import resolve, reverse

from ..views import PostList, PostDetail, CategoryDetail, CategoryList, CommentList, CommentDetail, ReplyList, \
    ReplyDetail


class PostTest(TestCase):

    def test_post_list(self):
        url = reverse('post_list')
        # print(url)
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail(self):
        url = reverse('post_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_category_list(self):
        url = reverse('category_list')
        self.assertEquals(resolve(url).func.view_class, CategoryList)

    def test_category_detail(self):
        url = reverse('category_details', args=[100])
        self.assertEquals(resolve(url).func.view_class, CategoryDetail)

    def test_comment_list(self):
        url = reverse('comment_list')
        self.assertEquals(resolve(url).func.view_class, CommentList)

    def test_comment_detail(self):
        url = reverse('comment_detail', args=[150000])
        self.assertEquals(resolve(url).func.view_class, CommentDetail)

    def test_reply_list(self):
        url = reverse('reply_list')
        self.assertEquals(resolve(url).func.view_class, ReplyList)

    def test_reply_detail(self):
        url = reverse('reply_detail', args=[100000])
        self.assertEquals(resolve(url).func.view_class, ReplyDetail)
