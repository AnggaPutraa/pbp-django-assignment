from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):

    def setUp(self):
        self.catalog = CatalogItem.objects.create(
            item_name = 'Panadol Paracetamol Ampuh',
            item_price =  300000,
            item_stock = 100000000000000000,
            description = 'Hilangkan pusing ketika nugas',
            rating = 5,
            item_url = 'https://www.tokopedia.com/topalembang/panadol-paracetamol-10-kaplet?extParam=ivf%3Dfalse%26src%3Dsearch', 
        )
    
    def test_create_catalog(self):
        self.assertEqual(
            self.catalog,
            CatalogItem.objects.get(
                item_name = 'Panadol Paracetamol Ampuh',
            ),
        )
