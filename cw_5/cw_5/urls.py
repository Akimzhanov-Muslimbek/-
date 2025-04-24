from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # маршруты твоего приложения posts
    path('accounts/', include('django.contrib.auth.urls')),  # добавляем маршруты для login/logout
]
