from django.test import TestCase
from .models import Category

class MyModelTestCase(TestCase):
    def test_create_model(self):
        """
        Test creating a new instance of MyModel.
        """
        my_object = Category.objects.create(
            name='value1',
            description='value2'
        )
        self.assertEqual(my_object.name, 'value1')
        self.assertEqual(my_object.description, 'value2')
