from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.PostList.as_view()),
    # path('contents/<int:pk>', views.post_detail),
    # path('category/', views.category_list),
]
