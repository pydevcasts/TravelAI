from django.test import TestCase
from .models import Post
from django.utils import timezone


class PostModelTest(TestCase):
    def setUp(self):
        """Create a Post instance for testing."""
        self.post = Post.objects.create(
            title="Test Post",
            description="This is a test post description.",
            icon="test_icon.png",
            published_at=timezone.now(),
        )

    def test_blog_creation(self):
        """Test if the post instance is created correctly."""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.description, "This is a test post description.")
        self.assertEqual(self.post.icon, "test_icon.png")
        self.assertIsNotNone(self.post.published_at)
        self.assertIsNotNone(self.post.created_at)
        self.assertIsNotNone(self.post.updated_at)

    def test_string_representation(self):
        """Test the string representation of the Post instance."""
        self.assertEqual(str(self.post), "Test Post")

    def test_default_published_at(self):
        """Test the default value of published_at."""
        blog_without_published_at = Post.objects.create(
            title="Another Post",
            description="Another description",
            icon="another_icon.png",
        )
        self.assertIsNotNone(blog_without_published_at.published_at)

    def test_blank_description(self):
        """Test that the description can be blank."""
        blog_with_blank_description = Post.objects.create(
            title="Post with Blank Description",
            description="",  # Set description to an empty string
            icon="blank_icon.png",
        )
        self.assertEqual(
            blog_with_blank_description.description, ""
        )  # Check if description is empty
