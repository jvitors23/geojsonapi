import pytest
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    def test_create_user_with_email_successful(self) -> None:
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "TestPass123"
        user = User.objects.create_user(email=email, password=password)

        assert user.email == email
        assert user.check_password(password)

    def test_new_user_email_normalized(self) -> None:
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = User.objects.create_user(email=email, password="saddsa123")

        assert user.email == email.lower()

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        msg = _("Users must have an email address.")
        with pytest.raises(ValueError, match=msg):
            User.objects.create_user(email=None, password="saddsa123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(email="test@gmail.com", password="test123")
        assert user.is_superuser
        assert user.is_staff
