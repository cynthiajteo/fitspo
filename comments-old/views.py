from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import *
from comments.forms import *
from comments.models import *
from django.http.response import HttpResponse, JsonResponse
import json


# Create your views here.

@login_required
def views_create(request, post):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(name=request.user,
                              comment=request.POST['comment'], post=post)
            comment.save()

            return redirect('posts:post_show', post.id)

    return render(request, 'posts/show.html', {'form': comment_form})
