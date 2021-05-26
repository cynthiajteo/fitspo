from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


# shows all posts on main page
@login_required
def view_index(request):
    posts = Post.objects.filter(hidden=False).order_by('-created_at')
    context = {'posts': posts}
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
@login_required
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


@login_required
def views_create_comment(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post)

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


# toggle like button
# @login_required
# def view_like(request, pk):
#     post = Post.objects.get(pk=pk)
#     like = Like.objects.get(post=pk)
#     like.liked = request.POST['liked'] == 'true'
#     like.save()
#     return render(request, 'posts:all_posts')
