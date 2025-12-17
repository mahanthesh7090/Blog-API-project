from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Posts


class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="postuser",
            password="postpass"
        )

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.post_data = {
            "title": "Test Post",
            "content": "Post content"
        }
    #for creating post
    def test_create_post(self):
        response = self.client.post("/posts", self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #get all posts
    def test_get_posts(self):
        Posts.objects.create(
            title="Post 1",
            content="Content",
            author=self.user
        )

        response = self.client.get("/posts")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #testing for non user
    def test_unauthorized_post_creation(self):
        self.client.credentials() 
        response = self.client.post("/posts", self.post_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #post update using post id test
    def test_update_post(self):
        post = Posts.objects.create(
            title="Old Title",
            content="Old Content",
            author=self.user
        )

        updated_data = {
            "title": "New Title",
            "content": "Updated content"
        }

        response = self.client.put(f"/posts/{post.id}", updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, "New Title")
    
    #For post deleting using id test
    def test_delete_post(self):
        post = Posts.objects.create(
            title="Delete Me",
            content="Delete content",
            author=self.user
        )

        response = self.client.delete(f"/posts/{post.id}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 0)