from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.user.api.serializers import UserSerializer


class UserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpass", email="testuser@example.com"
        )
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse("user-list")
        self.detail_url = reverse(
            "user-detail", kwargs={"username": self.user.username}
        )

    def test_user_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["username"], self.user.username)

    def test_user_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_user_create(self):
        data = {
            "username": "newuser",
            "password": "newpass",
            "email": "newuser@example.com",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(
            User.objects.get(username="newuser").email, "newuser@example.com"
        )

    def test_user_update(self):
        data = {"email": "updated@example.com"}
        response = self.client.patch(self.detail_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            User.objects.get(username=self.user.username).email, "updated@example.com"
        )

    def test_user_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        expected_fields = ["id", "username", "first_name", "last_name", "email"]
        self.assertEqual(set(serializer.data.keys()), set(expected_fields))
