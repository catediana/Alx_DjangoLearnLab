from django.shortcuts import render , redirect
from .models import Book
from .models import Library 
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render



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


def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

# role that checks the function for admin
def is_admin(user):
    try:
        return user.is_authenticated and user.userprofile.role == 'Admin'
    except AttributeError:
        return False

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

#View for users with the Admin role.
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("<h1>Welcome, Admin!</h1><p>This area is for administrative tasks.</p>")

# View for users with the Librarian role.
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

# View for users with the Member role.
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
