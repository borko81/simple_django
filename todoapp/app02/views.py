from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
        Post.objects.create(
            title=response_me['title'],
            description=response_me['description'],
            name=response_me['user']
        )
        return JsonResponse(response_me)

    if request.POST.get('action') == 'delete':
        id = request.GET.get('id')
        item = get_object_or_404(Post, id=id)
        item.delete()
        return JsonResponse(f'Successfully delete item with id {id}')
    return render(request, 'app02/index.html', {'posts': posts, 'user': show_user()})


def delid(request, id):
    item = get_object_or_404(Post, id=id)
    item.delete()
    return HttpResponse(f"Successfully delete item with id {id}")


def edit(request, id):
    if request.method == 'GET':
        item_data = {}
        item = get_object_or_404(Post, id=id)
        item_data['title'] = item.title
        item_data['description'] = item.description
        item_data['id'] = item.id
        item_data['name'] = item.name.id
        return JsonResponse(item_data)
    else:
        item = get_object_or_404(Post, id=id)
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        user_request = request.POST.get('name')
        item.name = User.objects.get(id=user_request)
        item.save()
        return HttpResponse('Success')
