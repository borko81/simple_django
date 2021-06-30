from django.shortcuts import render, redirect

from notes.forms import ProfileForms, NoteForms, NoteFormsDisabled
from notes.models import Profile, Note


def home_page(request):
    try:
        p = Profile.objects.all()[0]
        notes = Note.objects.all()
        return render(request, 'home-with-profile.html', {'notes': notes})
    except:
        form = ProfileForms()
        if request.method == 'POST':
            form = ProfileForms(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        return render(request, 'home-no-profile.html', {'form': form})


def add(request):
    form = NoteForms()
    if request.method == 'POST':
        form = NoteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'note-create.html', {'form': form})


def edit(request, id):
    note = Note.objects.get(id=id)
    form = NoteForms(instance=note)
    if request.method == 'POST':
        form = NoteForms(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'note-edit.html', {'form': form, 'note': note})


def delete(request, id):
    note = Note.objects.get(id=id)
    form = NoteFormsDisabled(instance=note)
    if request.method == 'POST':
        note.delete()
        return redirect('home_page')
    return render(request, 'note-delete.html', {'note': note, 'form': form})


def details(request, id):
    note = Note.objects.get(id=id)
    form = NoteForms(instance=note)
    return render(request, 'note-details.html', {'form': form, 'note': note})


def profile(request):
    p = Profile.objects.all()[0]
    notes = Note.objects.all().count()
    return render(request, 'profile.html', {'profile': p, 'notes': notes})


def delete_profile(request, id):
    p = Profile.objects.get(id=id)
    p.delete()
    Note.objects.all().delete()
    return redirect('home_page')
