from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    """
    Returns True if the user is authenticated, has a linked UserProfile,
    and their role is 'Admin'.
    """
    return (
        user.is_authenticated and 
        hasattr(user, 'userprofile') and 
        user.userprofile.role == 'Admin'
    )

@user_passes_test(is_admin)
def admin_view(request):
    """
    View that is accessible only to users with the 'Admin' role.
    """
    return HttpResponse("Welcome, Admin!")
