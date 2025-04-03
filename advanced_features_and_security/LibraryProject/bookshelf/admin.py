from django.contrib import admin
from .models import Book 
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    search_fields = ("title", "author")  
    list_filter = ("publication_year",)  

# Registering the Book model 
admin.site.register(Book, BookAdmin)

# 2.Integrating the Custom User Model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)



