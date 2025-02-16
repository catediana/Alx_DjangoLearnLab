# Delete a Book

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Delete the book
book.delete()

# Confirm deletion
print(Book.objects.all())  # Should return an empty queryset if the book was deleted successfully
