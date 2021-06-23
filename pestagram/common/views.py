from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from common.forms import CreatePetForm, CommentForm
from common.models import Pet, Like, Comment


def animals_count():
    count_animals = Pet.objects.all()
    return count_animals.count()


def index(request):
    return render(request, 'landing_page.html')


def pet_all(request):
    all_pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': all_pets})


def pet_detail(request, pk):
    pet_details = Pet.objects.get(pk=pk)
    likes = Like.objects.filter(pet=pet_details).count()
    comments = Comment.objects.all()

    if request.method == 'POST':
        comment = request.POST['comment']
        Comment.objects.create(comment=comment, pet=pet_details)
        return redirect('common:pet_detail', pk)
    form = CommentForm()
    return render(request, 'pet_detail.html', {'detail': pet_details, 'likes': likes, 'form': form, 'comment': comments})


def pet_like(request, pk):
    try:
        Like.objects.create(pet=Pet.objects.get(id=pk))
        return redirect('common:pet_detail', pk=pk)
    except:
        return HttpResponse(f'Not valid pk: {pk}')


def pets_create(request):
    form = CreatePetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('common:pet_all')
    return render(request, 'pet_create.html', {'form': form})


def pets_edit(request, pk):
    obj = Pet.objects.get(pk=pk)
    form = CreatePetForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('common:pet_all')

    return render(request, 'pet_edit.html', {'form': form})


def pets_delete(request, pk):
    obj = get_object_or_404(Pet, pk=pk)
    obj.delete()
    return redirect('common:pet_all')
