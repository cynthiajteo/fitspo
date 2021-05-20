from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def view_index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def view_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post(
                workout=request.POST['workout'],
                image=request.FILES['image'])
            post.save()
            return redirect('posts:all_posts')

    posts = Post.objects.all()
    context = {'form': form}
    return render(request, 'posts/create.html', context)


def view_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('posts:all_posts')

    # edit
    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:all_posts', post.id)

    if request.GET.get('action') == 'edit':
        form = PostForm(instance=post)
        context = {'post': post, 'edit': True, 'form': form}
        return redirect(request, 'posts/show.html', context)
