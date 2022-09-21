from rest_framework.decorators import api_view

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostList(APIView):
    """List all post or create posts"""

    def get(self, request):
        obj = Post.objects.all()
        serialize = PostSerializer(obj, many=True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serialize = PostSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """ retrieve, update and delete posts """

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serialize = PostSerializer(obj)
        return Response(serialize.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serialize = PostSerializer(obj, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request):
        obj = Category.objects.all()
        serialize = CategorySerializer(obj, many=True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serialize = CategorySerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_obj(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_obj(pk)
        serialize = CategorySerializer(obj)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_obj(pk)
        serialize = CategorySerializer(obj, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_obj(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from django.http import HttpResponse, JsonResponse
# from .models import Post, Category
# from .serializers import PostSerializer, CategorySerializer
#
#
# def post_list(request):
#     """
#     list all posts or create posts
#     """
#     if request.method == 'GET':
#         obj = Post.objects.all()
#         serialize = PostSerializer(obj, many=True)
#         return JsonResponse(serialize.data, safe=False)
#
#     elif request.method == 'POST':
#
#         serialize = PostSerializer(data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return JsonResponse(serialize.data, status=201)
#         return JsonResponse(serialize.errors, status=400)
#
#
# def post_detail(request, pk):
#     """ retrieve, update or delete code for posts"""
#
#     try:
#         obj = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serialize = PostSerializer(obj)
#         return JsonResponse(serialize.data)
#     elif request.method == 'PUT':
#         serialize = PostSerializer(obj, data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return JsonResponse(serialize.data)
#         return JsonResponse(serialize.errors, status=400)
#
#     elif request.method == 'DELETE':
#         obj.delete()
#         return HttpResponse(status=204)
#
#
# def category_list(request):
#     if request.method == 'GET':
#         obj = Category.objects.all()
#         serialize = CategorySerializer(obj, many=True)
#         return JsonResponse(serialize.data, safe=False)
#     elif request.method == 'POST':
#         serialize = CategorySerializer(data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return JsonResponse(serialize.data, status=201)
#         return JsonResponse(serialize.errors, status=400)
