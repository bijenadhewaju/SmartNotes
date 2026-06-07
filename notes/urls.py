from django.urls import path
from .views import NoteListCreate, note_list

urlpatterns = [
    path('notes/', NoteListCreate.as_view(), name='notes'),
    path('notes/home/', note_list, name='note_list'),
]
# test comment again
# another test comment