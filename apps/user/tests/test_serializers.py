from django.test import TestCase
from django.contrib.auth.models import User
from apps.user.api.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="usertest",
            email="usertest@test.com",
            first_name="User",
            last_name="Test User",
        )

        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(), ["id", "username", "email", "first_name", "last_name"]
        )

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.user.username, "usertest")
        self.assertEqual(data["username"], self.user.username)

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.user.email, "usertest@test.com")
        self.assertEqual(data["email"], self.user.email)

    def test_first_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.user.first_name, "User")
        self.assertEqual(data["first_name"], self.user.first_name)

    def test_last_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.user.last_name, "Test User")
        self.assertEqual(data["last_name"], self.user.last_name)
