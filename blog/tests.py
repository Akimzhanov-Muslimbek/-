from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Тестовый пост', content='Содержимое поста', author=self.user)

    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_unauthorized(self):
        data = {'title': 'Новый пост', 'content': 'Содержимое нового поста'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_authorized(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Новый пост', 'content': 'Содержимое нового поста'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, content='Test Comment', author=self.user)

    def test_create_comment(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'post': self.post.id, 'content': 'New Comment'}
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostFilterSearchTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = Post.objects.create(title='First Post', content='Content of the first post', author=self.user)
        self.post2 = Post.objects.create(title='Second Post', content='Content of the second post', author=self.user)

    def test_filter_posts_by_author(self):
        response = self.client.get(f'/api/posts/?author={self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_posts_by_title(self):
        response = self.client.get('/api/posts/?search=First')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'First Post')
