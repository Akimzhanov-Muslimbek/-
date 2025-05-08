from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.urls import path
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAuthorOrReadOnly

# Create your views here.

def home(request):
    return HttpResponse("Добро пожаловать в API проекта Sessia!")

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']  # Фильтрация по автору
    search_fields = ['title', 'content']  # Поиск по заголовку и содержимому
    ordering_fields = ['created_at', 'title']  # Сортировка по дате создания и заголовку

    @swagger_auto_schema(
        operation_description="Получить список постов",
        responses={200: PostSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']  # Фильтрация по автору
    search_fields = ['title', 'content']  # Поиск по заголовку и содержимому
    ordering_fields = ['created_at', 'title']  # Сортировка по дате создания и заголовку

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['post', 'author']  # Фильтрация по посту и автору
    search_fields = ['content']  # Поиск по содержимому комментария
    ordering_fields = ['created_at']  # Сортировка по дате создания

urlpatterns = [
    path('', home, name='home'),  # Корневой маршрут
]
