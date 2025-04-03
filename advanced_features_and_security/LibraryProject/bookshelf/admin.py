from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import Book, CustomUser

# Custom BookAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")  
    search_fields = ("title", "author")  
    list_filter = ("published_date",)  

# Register Book Model
admin.site.register(Book, BookAdmin)  

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )

# Register Custom User Model
admin.site.register(CustomUser, CustomUserAdmin)

# Setup Groups & Assign Permissions
def setup_groups():
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    try:
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        viewers.permissions.add(can_view)
        editors.permissions.add(can_view, can_create, can_edit)
        admins.permissions.add(can_view, can_create, can_edit, can_delete)
    except Permission.DoesNotExist:
        print("⚠️ Permissions not found! Run `python manage.py migrate` first.")

setup_groups()
