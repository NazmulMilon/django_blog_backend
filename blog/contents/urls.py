from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.PostList.as_view()),
    path('contents/<int:id>/', views.PostDetail.as_view()),
]
