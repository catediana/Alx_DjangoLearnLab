from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    # Check that the user is authenticated, has a UserProfile, and role equals 'Admin'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
     return HttpResponse("<h1>Welcome, Admin!</h1><p>This area is for administrative tasks.</p>")
