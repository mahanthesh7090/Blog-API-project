from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Posts

from django.test import TestCase
from app.serializers import CommentSerializer

#comment serializtion unit test
class CommentSerializerTest(TestCase):

    def test_comment_serializer_invalid_without_content(self):
        data = {
            "content": ""
        }
        serializer = CommentSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("content", serializer.errors)

#user and posts serialization unit test
class PostModelTest(TestCase):

    def test_post_str_method_returns_title(self):
        user = User.objects.create_user(username="testuser", password="pass123")
        post = Posts.objects.create(
            title="My First Post",
            content="Post content",
            author=user
        )

        self.assertEqual(str(post), "My First Post")
