from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class FoundationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="teste", password="test-password-123")

    def test_home_requires_login(self):
        self.assertRedirects(self.client.get(reverse("home")), "/login/?next=/")

    def test_login_and_logout(self):
        response = self.client.post(reverse("login"), {"username": "teste", "password": "test-password-123"})
        self.assertRedirects(response, reverse("home"))
        self.assertContains(self.client.get(reverse("home")), "teste")
        self.assertRedirects(self.client.post(reverse("logout")), reverse("login"))
        self.assertRedirects(self.client.get(reverse("home")), "/login/?next=/")

    def test_non_staff_cannot_access_admin(self):
        self.client.force_login(self.user)
        self.assertRedirects(self.client.get(reverse("admin:index")), "/admin/login/?next=/admin/")

    def test_admin_access(self):
        admin = get_user_model().objects.create_superuser("admin-test", password="test-password-123")
        self.client.force_login(admin)
        self.assertEqual(self.client.get(reverse("admin:index")).status_code, 200)
