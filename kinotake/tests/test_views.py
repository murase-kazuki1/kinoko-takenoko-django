from django.test import TestCase
from django.urls import reverse
from ..models import Vote

# Create your tests here.
class IndexTests(TestCase):

    def test_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
