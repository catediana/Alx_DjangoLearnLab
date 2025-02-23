from django.shortcuts import render
from .models import Book, Library 
from django.views.generic.detail import DetailView
from django.http import HttpResponse


# Function-based view that lists all books in the database.


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
