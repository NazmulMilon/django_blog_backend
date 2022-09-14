from django.shortcuts import render
from .models import Category, Post


# Create your views here.

def homepage(request):
    post = Post.objects.all()

    context = {
        'post': post,
    }
    return render(request, 'display.html', context)
