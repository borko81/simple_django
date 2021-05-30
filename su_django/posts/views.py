from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, Like


def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse('success like button')
    else:
        return HttpResponse('unsuccess')
