from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch
from advancedMethods.models import *
from django.test import TestCase, override_settings
from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent.parent


# @override_settings(DATABASES={
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# })

class AdvancedMethodsTestCase(APITestCase):
    def setup(self):
        pass

    def test_get_endpoint(self):
        response = self.client.get("/api/advanced-methods-api/test-table-1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn("id", response.json())
    
    def test_post_endpoint(self):
        data = {
            "col_1": "Hello",
            "col_2": "Hello 1",
            "col_3": "Hello 2"
        }
        response = self.client.post("/api/advanced-methods-api/test-table-1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#testing with decorator function
class LocationListAPIViewDecoratorTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(name="Test Location")
        Products.objects.create(name="Test Product", location_id=self.location, price=44)
    
    # def test_authentication_successfull(self):
    #     # self.client.credentials(HTTP_LOCATION_ID=self.location.id, HTTP_ADMIN_ID=1)
    #     response = self.client.get("/api/advanced-methods-api/location-list-api-view/", content_type="application/json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_endpoint(self):
        response = self.client.get("/api/advanced-methods-api/location-list-api-view/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn("id", response.json())
    
