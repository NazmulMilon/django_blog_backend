from django.urls import path
from . import views
# from .views import PostList, PostDetail, CategoryList, CategoryDetail

urlpatterns = [
    # path('', views.home_page(), name='home'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),

]
