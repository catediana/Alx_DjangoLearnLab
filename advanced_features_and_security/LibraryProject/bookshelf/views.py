from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book

# enforcing permission checks allowing users to perform certain actions.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse({'books': books}, safe=False)

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return JsonResponse({'message': 'You have permission to create a book'})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse({'message': f'You can edit the book: {book.title}'})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse({'message': f'You can delete the book: {book.title}'})



