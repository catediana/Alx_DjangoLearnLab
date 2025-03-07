from django.shortcuts import render , redirect
from .models import Book
from .models import Library 
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


#serving login.html as homepage
def home(request):
    return render(request, 'login.html')

# Function-based view that lists all books in the database.

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

#class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



 # view for user registration 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
