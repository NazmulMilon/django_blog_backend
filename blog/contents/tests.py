from django.test import TestCase

# Create your tests here.
from .models import Category
from django.utils import timezone
from django.core.urlresolvers import reverse


class CategoryTest(TestCase):
    def create_category(self, title="only a test", body="only a body test"):
        return Category.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w, __unicode__(), w.title)
