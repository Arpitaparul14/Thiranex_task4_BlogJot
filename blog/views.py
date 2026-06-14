from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.text import slugify
from .models import Post, Category, Comment, Like, Notification
from .forms import PostForm, CommentForm, RegisterForm


def home(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories, 'selected': category_slug})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(post=post, user=request.user).exists()
    comment_form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to comment.')
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            if post.author != request.user:
                Notification.objects.create(
                    user=post.author,
                    sender=request.user,
                    notif_type='comment',
                    message=f'{request.user.username} commented on your post "{post.title}"',
                    post=post
                )
            messages.success(request, 'Comment added!')
            return redirect('post_detail', slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'liked': liked,
        'like_count': post.likes.count(),
        'comment_form': comment_form,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit'})


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    else:
        if post.author != request.user:
            Notification.objects.create(
                user=post.author,
                sender=request.user,
                notif_type='like',
                message=f'{request.user.username} liked your post "{post.title}"',
                post=post
            )
    return redirect('post_detail', slug=slug)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created! Welcome to BlogJot!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})


@login_required
def notifications(request):
    notifs = Notification.objects.filter(user=request.user)
    notifs.filter(is_read=False).update(is_read=True)
    return render(request, 'blog/notifications.html', {'notifications': notifs})