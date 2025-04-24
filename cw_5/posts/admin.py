from django.contrib import admin
from .models import Post # Импортируем вашу модель Post

admin.site.register(Post) # Регистрируем модель Post