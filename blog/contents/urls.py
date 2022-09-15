from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.post_list),
]
