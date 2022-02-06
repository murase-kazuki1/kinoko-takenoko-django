from django.test import TestCase
from django.urls import reverse, resolve
from ..views import index, vote

# Create your tests here.
class TestUrls(TestCase):

    def test_post_index_url(self):
        view = resolve('/')
        self.assertEqual(view.func, index)


    def test_post_vote_url(self):
        view = resolve('/vote')
        self.assertEqual(view.func, vote)
