from django.http import HttpResponse, JsonResponse
from .models import Post
from .serializers import PostSerializer


def post_list(request):
    """
    list all posts or create posts
    """
    if request.method == 'GET':
        obj = Post.objects.all()
        serialize = PostSerializer(obj, many=True)
        return JsonResponse(serialize.data, safe=False)

    elif request.method == 'POST':
        serialize = PostSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=201)
        return JsonResponse(serialize.errors, status=400)

