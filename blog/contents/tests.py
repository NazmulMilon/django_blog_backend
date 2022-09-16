from django.test import TestCase

# Create your tests here.
from .models import Category, Post
from django.utils import timezone


# from django.core.urlresolvers import reverse
# from contents.forms improt CategoryForm

class CategoryTest(TestCase):
    def create_category(self, category_name="only a test"):
        return Category.objects.create(category_name=category_name)

    def test_category_creation(self):
        category_obj = self.create_category()
        self.assertTrue(isinstance(category_obj, Category))
        self.assertEqual(category_obj.category_name, category_obj.category_name)
