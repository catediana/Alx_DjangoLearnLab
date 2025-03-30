from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    """
    Check if the user is authenticated, has an associated UserProfile,
    and that their role is 'Admin'.
    """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    """
    An Admin view that only users with the 'Admin' role can access.
    """
    return HttpResponse("Welcome, Admin!")
