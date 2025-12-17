from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import  Comment,Posts

class CommentAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="commentuser",
            password="commentpass"
        )

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        self.post = Posts.objects.create(
            title="Post",
            content="Content",
            author=self.user
        )

        self.comment = Comment.objects.create(
        post=self.post,
        content="Nice post!",
        author=self.user
    )

    def test_create_comment(self):
        response = self.client.post("/comments", {
            "post": self.post.id,
            "content": "Another comment"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #commment update test
    def test_update_comment(self):
        updated_data = {
            "content": "Updated comment text"
        }

        response = self.client.patch(
            f"/comments/{self.comment.id}",
            updated_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, "Updated comment text")

    #Delete test
    def test_delete_comment(self):
        response = self.client.delete(
            f"/comments/{self.comment.id}"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)