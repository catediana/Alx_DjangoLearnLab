from django.test import TestCase, Client
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

class AdminViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create admin user and profile explicitly
        self.admin_user = User.objects.create_user(username='admin', password='moha@22nov')
        UserProfile.objects.create(user=self.admin_user, role='Admin')
    
    def test_admin_view_access(self):
        self.client.login(username='admin', password='moha@22nov')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_non_admin_access(self):
        non_admin_user = User.objects.create_user(username='nonadmin', password='nonadminpassword')
        UserProfile.objects.create(user=non_admin_user, role='Member')
        self.client.login(username='nonadmin', password='nonadminpassword')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 403)  # Now expects 403
