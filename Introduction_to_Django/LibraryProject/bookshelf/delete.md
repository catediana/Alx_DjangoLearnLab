from bookshelf.models import Book

books = Book.objects.filter(title="Nineteen Eighty-Four")
print(books)  # Show all books with this title
books.delete()
print("Books deleted successfully.")
