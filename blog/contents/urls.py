from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.post_list),
    path('contents/<int:pk>', views.post_detail)
]
