from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Posts, Comment

class AuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_login(self):
        response = self.client.post("/api/token/", {
            "username": "testuser",
            "password": "testpass123"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)