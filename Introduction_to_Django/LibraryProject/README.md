��� LibraryProject
��� Overview
LibraryProject is a Django-based web application designed to manage a digital library system. This project serves as a foundation for learning Django and developing web applications with features like book management, user authentication, and borrowing records.

�� Features
Django framework setup
Database configuration
User authentication system (future feature)
Book catalog management (future feature)
Borrowing and return tracking (future feature)


from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"{book.title} by {book.author} ({book.publication_year})")

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)  
​

# Retrieving Book Data

## Command:
```python


from bookshelf.models import Book
book = Book.objects.filter(title="1984").first()
if book:
    print(book.title, book.author, book.publication_year)
else:
    print("No book found with that title.")


books = Book.objects.filter(title="1984")
if books.count() > 1:
    books[1:].delete()  # Keep only the first book, delete the rest
book = Book.objects.get(title="1984")  # Now it should work


from bookshelf.models import Book

books = Book.objects.filter(title="Nineteen Eighty-Four")
print(books)  # Show all books with this title
books.delete()
print("Books deleted successfully.")
