# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from . import admin_view, librarian_view, member_view  # Import the role-based view files
from .views import (
    list_books, LibraryDetailView, register,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for showing library details
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
     
     #login view using django bult in logon view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout view using Django's built-in LogoutView with a custom template
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Registration view using your custom view
    path('register/', views.register, name='register'),

    # URL patterns to route the role‑specific views
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

#views for secure paths
    path('add_book/', views.add_book, name='add_book'),  # Change 'add/' to 'add_book/'
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Change 'edit/' to 'edit_book/'
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Optional if needed
]