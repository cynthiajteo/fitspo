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
    # workoutForm = WorkoutForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post(
                workout=request.POST['workout'],
                image=request.FILES['image'])
            post.save()
            return redirect('/')

    posts = Post.objects.all()
    context = {'form': form}
    return render(request, 'posts/create.html', context)
