from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


@login_required
def view_index(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-created_at')
    posts = Post.objects.filter(hidden=False)
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


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


@login_required
def view_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    if request.GET.get('action') == 'del':
        post.delete()
        return redirect('posts:all_posts')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = EditForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:post_show', post.id)

    if request.GET.get('action') == 'edit':
        form = EditForm(instance=post)

        context = {'post': post, 'edit': True, 'form': form}
        return render(request, 'posts/show.html', context)

    context = {"post": post, "edit": False}
    return render(request, 'posts/show.html', context)
