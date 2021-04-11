from django.shortcuts import render, get_object_or_404
from . models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'bookblog/list.html',
        {
            'posts': posts,
            'title': 'all posts',
        }
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(
        request,
        'bookblog/detail.html',
        {
            'post': post,
            'title': 'detail posts',
        }
    )
