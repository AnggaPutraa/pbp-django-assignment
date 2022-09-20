from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_my_watch_list, show_my_watchlist_json, show_my_watchlist_xml

class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'mywatchlist:show_my_watch_list'
        )
        self.urlToViewJson = reverse(
            'mywatchlist:show_my_watchlist_json'
        )
        self.urlToViewXML = reverse(
            'mywatchlist:show_my_watchlist_xml'
        )

    def test_my_wish_list_urls_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewHtml
            ).func,
            show_my_watch_list
        )
        
    def test_my_wish_list_xml_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewJson
            ).func,
            show_my_watchlist_json
        )

    def test_my_wish_list_json_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewXML
            ).func,
            show_my_watchlist_xml
        )
