from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@gmail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the Tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegen'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
