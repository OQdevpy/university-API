from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.db.models import Q

from .permissions import IsOwnerOrReadOnly
from ...models import Category, Tag, Blog
from .serializers import CategorySerializer, TagSerializer, BlogSerializer


class CategoryListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/category-list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/tag-list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BLogListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-list-create/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<id>/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]


