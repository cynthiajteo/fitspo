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
        form = PostForm(request.POST)
        # workoutForm = WorkoutForm(request.POST)
        if form.is_valid():
            post = Post(image=request.POST['image'])
            post.save()
        # if workoutForm.is_valid():
        #     workout = Workout(workout=request.POST['workout'])
        #     workout.save()
    posts = Post.objects.all()
    # workouts = Workout.objects.all()
    context = {'form': form}
    return render(request, 'posts/create.html', context)
