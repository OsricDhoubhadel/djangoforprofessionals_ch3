from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="will@email.com", username="will", password="testpass123"
        )
        self.assertEqual(user.email, "will@email.com")
        self.assertEqual(user.username, "will")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="superadmin@email.com", username="superadmin", password="testpass123"
        )
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertEqual(admin_user.username, "superadmin")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
