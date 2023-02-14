from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
# Create your tests here.


class ProductTests(APITestCase):

    def test_view_product(self):
        url = reverse('base:home_api')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
