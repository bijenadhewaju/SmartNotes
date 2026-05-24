from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


def note_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Note.objects.create(
                title=title,
                content=content
            )

        return redirect('note_list')

    notes = Note.objects.all()

    return render(
        request,
        'notes/notes.html',
        {'notes': notes}
    )