from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Просмотр всех постов
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})  # Убедитесь, что путь совпадает

# Просмотр деталей поста
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    can_edit = request.user == post.author or request.user.is_superuser
    return render(request, 'post_detail.html', {'post': post, 'can_edit': can_edit})

# Создание нового поста
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Удаление поста
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect('posts_list')
