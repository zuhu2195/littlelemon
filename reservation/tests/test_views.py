from django.test import TestCase
#from ..views import 
from ..models import Menu
from ..serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Kebab", price="100", inventory=20)
        self.item1.save()
        self.item2 = Menu.objects.create(title="Beef Ribs", price="800", inventory=10)
        self.item2.save()
        self.user = User.objects.create_user(username="zuhu", password="123456")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Make a GET request to the view
        url = reverse("menu-list")  # use your actual URL name (e.g., path('menu/', MenuView.as_view(), name='menu-list'))
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def tearDown(self):
        self.item1.delete()
        self.item2.delete()
