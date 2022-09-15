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


def post_detail(request, pk):
    """ retrieve, update or delete code for posts"""

    try:
        obj = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialize = PostSerializer(obj)
        return JsonResponse(serialize.data)
    elif request.method == 'PUT':
        serialize = PostSerializer(obj, data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data)
        return JsonResponse(serialize.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
