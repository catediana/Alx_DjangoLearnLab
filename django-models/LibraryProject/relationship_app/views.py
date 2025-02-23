from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.http import HttpResponse


# Function-based view that lists all books in the database.

def list_books(request):
    books = Book.objects.all()
    output = "Books Available:\n\n"
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return HttpResponse(output, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
