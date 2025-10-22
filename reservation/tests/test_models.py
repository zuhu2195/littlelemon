from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price="100", inventory=20)
        self.assertEqual(str(item), "IceCream : 100")