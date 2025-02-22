# Retrieve all books with title "1984"
books = Book.objects.filter(title="1984")

if books.exists():
    for book in books:
        book.title = "Nineteen Eighty-Four"
        book.save()
        print(f"Updated: {book.title}, {book.author}, {book.publication_year}")
 else:
        print("Error: The book with title '1984' does not exist.")
