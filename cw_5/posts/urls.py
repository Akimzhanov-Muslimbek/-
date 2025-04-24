from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),  # Список постов на корневом пути
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
