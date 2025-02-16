# CRUD Operations in Django ORM

## í´¹ 1. Create a Book
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


 2. Retrieve a Book
 book = Book.objects.get(title="1984")
 print(book.title, book.author, book.publication_year)



  Update a Book

  book = Book.objects.get(title="1984")
  book.title = "Nineteen Eighty-Four"
  book.save()
  print(book.title)


  4. Delete a Book
  book = Book.objects.get(title="Nineteen Eighty-Four")
  book.delete()

  remaining_books = Book.objects.filter(title="Nineteen Eighty-Four")
  print(remaining_books)

  
