from accounts.models import User, Profile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from posts.models import *


# register/sign up
def views_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, "Password is not a match")
            return render(request, "accounts/register.html")

        try:
            pass
            user = User.objects.create_user(username, email, password,
                                            first_name=first_name, last_name=last_name)

            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            messages.error(request, "Username is taken")
            return render(request, 'accounts/register.html')

        login(request, user)
        return redirect("posts:all_posts")

    else:
        form = UserCreationForm()  # django form inbuilt
        return render(request, "accounts/register.html", {"form": form})


# login
def views_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # wrong username
        try:
            username = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "user not found")
            return render(request, 'accounts/login.html')

        # if user exists is active
        if user is not None and user.is_active:
            login(request, user)
            return redirect("posts:all_posts")
        else:
            # wrong password
            messages.error(
                request, "password is incorrect, try again")
    return render(request, "accounts/login.html")


# logout
def views_logout(request):
    logout(request)
    return redirect('accounts:login')


# view other profiles
@login_required
def views_others(request, user_id=None):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('posts:all_posts')
    posts = Post.objects.filter(
        name_id=user_id, hidden=False).order_by('-created_at')
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'user': user, 'page_obj': page_obj}
    return render(request, 'accounts/profile.html', context)


# personal profile view
@login_required
def views_profile(request):
    try:
        user = User.objects.filter(pk=request.user.id).first()
    except User.DoesNotExist:
        return redirect('posts:all_posts')

    posts = Post.objects.filter(
        name=request.user.id, hidden=False).order_by('-created_at')
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'accounts/profile.html', context)
