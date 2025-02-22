from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    # Establishes a many-to-one relationship: many books to one author.
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, 
        related_name='books'
    )


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(
        Book,
        related_name = 'Library'
    )
    

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,  # use the Library class, not "library"
        on_delete=models.CASCADE,  
        related_name='librarian'
    )
