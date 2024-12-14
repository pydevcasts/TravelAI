
from django.test import TestCase
from .models import Blog
from django.utils import timezone

class BlogModelTest(TestCase):

    def setUp(self):
        """Create a Blog instance for testing."""
        self.blog = Blog.objects.create(
            title='Test Blog',
            description='This is a test blog description.',
            icon='test_icon.png',
            published_at=timezone.now()
        )

    def test_blog_creation(self):
        """Test if the blog instance is created correctly."""
        self.assertEqual(self.blog.title, 'Test Blog')
        self.assertEqual(self.blog.description, 'This is a test blog description.')
        self.assertEqual(self.blog.icon, 'test_icon.png')
        self.assertIsNotNone(self.blog.published_at)
        self.assertIsNotNone(self.blog.created_at)
        self.assertIsNotNone(self.blog.updated_at)

    def test_string_representation(self):
        """Test the string representation of the Blog instance."""
        self.assertEqual(str(self.blog), 'Test Blog')

    def test_default_published_at(self):
        """Test the default value of published_at."""
        blog_without_published_at = Blog.objects.create(
            title='Another Blog',
            description='Another description',
            icon='another_icon.png'
        )
        self.assertIsNotNone(blog_without_published_at.published_at)

    def test_blank_description(self):
        """Test that the description can be blank."""
        self.assertIsNone(self.blog.description)
