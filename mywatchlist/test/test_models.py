from django.test import TestCase
from mywatchlist.models import WatchItem

class TestModels(TestCase):

    def setUp(self):
        self.watchItem = WatchItem.objects.create(
            watched = True,
            title = 'Hustle',
            rating = 3,
            release_date = 'June 8, 2022',
            review = 'This was a great mix of the greatest sports films ever made and it feels on its own at the same time.',
        )

    def test_create_watch_item(self):
        self.assertEqual(
            self.watchItem,
            WatchItem.objects.get(
                title = 'Hustle'
            )
        )
