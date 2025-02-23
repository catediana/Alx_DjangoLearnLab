from django.shortcuts import render
from .models import Book
from .models import Library 
from django.views.generic.detail import DetailView



# Function-based view that lists all books in the database.


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

#class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
