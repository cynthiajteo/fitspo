from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm


def views_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, "password is not a match")
            return render(request, "accounts/register.html")

        try:
            pass
            user = User.objects.create_user(username, email, password,
                                            first_name=first_name, last_name=last_name)

            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            messages.error(request, "Username is taken already")
            return render(request, 'accounts/register.html')

        login(request, user)
        return redirect("posts:all_posts")
        # return render(request, "accounts/register.html")
    else:
        form = UserCreationForm()  # django form inbuilt
        return render(request, "accounts/register.html", {"form": form})


def views_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # if user is not empty, then login
        if user is not None:
            login(request, user)
            return redirect("posts:all_posts")
            # return render(request, "accounts/register.html")
        else:
            messages.error(request, "username or password is incorrect")
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")


def views_logout(request):
    logout(request)
    return redirect('accounts:login')
