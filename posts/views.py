from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django import template


# Create your views here.
# shows all posts on main page
@login_required
def view_index(request):
    posts = Post.objects.filter(hidden=False).order_by('-created_at')
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    allLikes = Like.objects.filter(liked=True)
    userLikes = Like.objects.filter(liked=True, user_id=request.user)
    countLikes = Like.objects.filter(liked=True, user_id=request.user).count

    context = {'posts': posts, 'userLikes': userLikes, 'allLikes': allLikes, 'countLikes': countLikes,
               'page_obj': page_obj}

    return render(request, 'posts/index.html', context)


# create new post
@login_required
def view_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post(
                workout=request.POST['workout'],
                image=request.FILES['image'],
                name=request.user)
            post.save()
            return redirect('posts:all_posts')

    posts = Post.objects.all()
    context = {'form': form}
    return render(request, 'posts/create.html', context)


# edit form
@login_required
def view_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    if request.user == post.name:
        if request.GET.get('action') == 'del':
            post.delete()
            return redirect('posts:all_posts')

        if request.method == 'POST' and request.GET['action'] == 'edit':
            form = EditForm(request.POST, request.FILES, instance=post)

            if form.is_valid():
                form.save()
                return redirect('posts:all_posts')

        if request.GET.get('action') == 'edit':
            form = EditForm(instance=post)

            context = {'post': post, 'edit': True, 'form': form}
            return render(request, 'posts/edit.html', context)

    else:
        if request.user.is_superuser:
            if request.GET.get('action') == 'del':
                post.delete()
                return redirect('posts:all_posts')

        context = {"post": post, "edit": False}
        return render(request, 'posts/others.html', context)

    context = {"post": post, "edit": False}
    return render(request, 'posts/edit.html', context)


# show post
@ login_required
def view_show_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.user == post.name:
        if request.GET.get('action') == 'del':
            post.delete()
            return redirect('posts:all_posts')

        if request.GET.get('action') == 'edit':
            form = EditForm(request.POST, request.FILES, instance=post)

            if form.is_valid():
                form.save()
                return redirect('posts:all_posts')

            context = {'post': post, 'comments': comments,
                       'edit': True, 'form': form}
            return render(request, 'posts/edit.html', context)
    else:
        if request.user.is_superuser:
            if request.GET.get('action') == 'del':
                post.delete()
                return redirect('posts:all_posts')

        context = {"post": post, 'comments': comments, "edit": False}
        return render(request, 'posts/others.html', context)

    context = {"post": post, 'comments': comments, "edit": False}
    return render(request, 'posts/show.html', context)


# create comment
@login_required
def views_create_comment(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(name=request.user,
                              comment=request.POST['comment'], post=post)
            comment.save()
            return redirect('posts:post_show', post.id)

    context = {'post': post, 'comments': comments,
               'comment_form': comment_form, }
    return render(request, 'posts/comments.html', context)


# like button
@login_required
def view_like(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if Like.objects.filter(user_id=request.user.id, post=post).exists():
            like = Like.objects.get(user_id=request.user.id, post=post)

            if Like.objects.filter(liked=False, post=post, user_id=request.user.id):
                Like.objects.filter(liked=False, post=post,
                                    user_id=request.user.id).update(liked=True)
                return redirect('posts:all_posts')

            elif Like.objects.filter(liked=True):
                like.liked = False
                like.save()
                return redirect('posts:all_posts')
        else:
            like = Like.objects.create(
                user_id=request.user.id, post=post, liked=True)
            like.save()
            return redirect('posts:all_posts')


# user's likes page
@login_required
def view_user_likes(request):
    try:
        user = User.objects.filter(pk=request.user.id).first()
    except User.DoesNotExist:
        return redirect('posts:all_posts')
    post = Post.objects.all()
    likes = Like.objects.filter(
        user=request.user.id, liked=True).order_by('-created_at')
    paginator = Paginator(likes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'likes': likes, 'post': post, 'page_obj': page_obj}
    return render(request, 'posts/likes.html', context)
