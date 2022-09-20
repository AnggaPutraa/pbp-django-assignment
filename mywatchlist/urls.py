from django.urls import path
from mywatchlist.views import show_my_watch_list, show_my_watchlist_json, show_my_watchlist_xml, show_my_wishlist_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_my_watch_list, name = 'show_my_watch_list'),
    path('json/', show_my_watchlist_json, name = 'show_my_watchlist_json'),
    path('xml/', show_my_watchlist_xml, name = 'show_my_watchlist_xml'),
    path('html/', show_my_wishlist_html, name = 'show_my_wishlist_html'),
]