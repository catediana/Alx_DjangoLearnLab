# Rtrieving Book data
from bookshelf.models import Book
book = Book.objects.filter(title="1984").first()
if book:
    print(book.title, book.author, book.publication_year)
    else:
        print("No book found with that title.")

