from django.http import JsonResponse
from django.shortcuts import render

from app02.models import Post, User


def show_user():
    user = User.objects.all()
    return user


def index(request):
    posts = Post.objects.all()
    response_me = {}
    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        name = request.POST.get('name')

        response_me['title'] = title
        response_me['description'] = description
        user = name
        response_me['user'] = User.objects.get(id=user)
        print(response_me)
        Post.objects.create(
            title=response_me['title'],
            description=response_me['description'],
            name=response_me['user']
        )
        return JsonResponse(response_me)
    return render(request, 'app02/index.html', {'posts': posts, 'user': show_user()})
