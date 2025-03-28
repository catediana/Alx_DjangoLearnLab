# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views
from relationship_app.views import admin_view ,librarian_view , member_view 

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
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

 ]