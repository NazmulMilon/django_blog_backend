from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer


def post_list(request):
    """list all posts or create posts"""
    if request.method == 'GET':
        obj = Post.objects.all()
        serializer = PostSerializer(obj, many=True)
        return HttpResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400 )

