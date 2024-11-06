from rest_framework import serializers
from django.test import TestCase
from advancedMethods.serializer import *
from advancedMethods.models import *


class TestSerializersTest(TestCase):
    def test_valid_data(self):
        data = {
            "role_name":"admin",
            "permissions":{
                "Create":True,
                "Read":True
            }
        }
        serializer = userRoleSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    
    def test_invalid_data(self):
        data = {
            "role_name":"",
            "permissions":{
                "Create":True,
                "Read":True
            }
        }
        serializer = userRoleSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("role_name", serializer.errors)

