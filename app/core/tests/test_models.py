from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = "test@mydomain.com"
        password = "my1234password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """test the email for a new user is normalized"""
        email = 'test@MYDOMAIN.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='my1234password'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'my1234password')

    def test_create_new_supperuser(self):
        """testing creation of super user"""

        user = get_user_model().objects.create_superuser(
            "test@mydomain.com",
            'my1234password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
