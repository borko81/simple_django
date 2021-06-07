from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from common.models import Pet, Like


def index(request):
    return render(request, 'landing_page.html')


def pet_all(request):
    all_pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': all_pets})


def pet_detail(request, pk):
    pet_details = get_object_or_404(Pet, id=pk)
    likes = Like.objects.filter(pet=pet_details).count()
    return render(request, 'pet_detail.html', {'detail': pet_details, 'likes': likes})


def pet_like(request, pk):
    try:
        Like.objects.create(pet=Pet.objects.get(id=pk))
        return redirect('common:pet_detail', pk=pk)
    except:
        return HttpResponse(f'Not valid pk: {pk}')
