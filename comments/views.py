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
    form = CommentForm()
    if request.method == 'POST':
        post = Post.objects.get(pk=post)
        form = CommentForm(request.POST)
        if form.is_valid():
            # form.save()
            # 1
            # review = Review(name=request.POST['name'], review=request.POST['review'],
            #   book=book)
            # review.save()

            # 2
            post = Post.objects.get(pk=post)
            post.comments.create(
                name=request.POST['name'], comment=request.POST['comment'])

            return redirect('posts:post_show', post.id)
    return HttpResponse({"message": "works"})
