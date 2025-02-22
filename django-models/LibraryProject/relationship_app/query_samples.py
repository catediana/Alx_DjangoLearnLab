from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):

    #Querying all books by a specific author.
    try:
        author = Author.objects.filter(author=author)
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f" These Books were wrote by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name: {author_name}")

def query_books_in_library(library_name):
    #Listing all books in a library.
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")

def query_librarian_of_library(librarian_name):
    """Retrieve the librarian for a specific library."""
    try:
        librarian= Librarian.objects.get(library=librarian_name)
       
        print(f"Librarian for library  {librarian.name}")
    
    except Librarian.DoesNotExist:
        print("No librarian assigned to the library")

