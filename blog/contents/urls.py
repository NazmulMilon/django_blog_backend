from django.urls import path
from . import views

# from .views import PostList, PostDetail, CategoryList, CategoryDetail

# app_name = 'contents'
urlpatterns = [
    # path('', views.get_posts, name='get_posts'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),

    path('comment/', views.CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),

    path('reply/', views.ReplyList.as_view(), name='reply_list'),
    path('reply/<int:pk>/', views.ReplyDetail.as_view(), name='reply_detail'),
]
