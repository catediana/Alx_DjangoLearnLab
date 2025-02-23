# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for showing library details; expects a library primary key
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

