from django.contrib import admin
 # Import the Book model
from .models import Book 

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    search_fields = ("title", "author")  
    list_filter = ("publication_year",)  

# Registering the Book model 
admin.site.register(Book, BookAdmin)


