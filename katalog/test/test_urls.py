from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestViews(TestCase):

    def setUp(self):
        self.url = reverse(
            'katalog:show_katalog',
        )

    def test_katalog_urls_resolve(self):
        self.assertEqual(
            resolve(
                self.url
            ).func,
            show_katalog,
        )