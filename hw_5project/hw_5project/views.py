# hw_5project/views.py

from django.shortcuts import render  # Импортируем render для отображения шаблонов

def home(request):
    return render(request, 'home.html')  # Отображаем шаблон 'home.html' на главной странице
