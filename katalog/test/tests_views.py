from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.clent = Client()
        self.url = reverse(
            'katalog:show_katalog',
        )

    def test_views_is_resolve(self):
        self.response = self.client.get(
            self.url
        )
        self.assertEqual(
            self.response.status_code,
            200
        )
        self.assertTemplateUsed(
            self.response,
            'katalog.html'
        )
