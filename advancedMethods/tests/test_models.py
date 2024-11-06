from django.test import TestCase
from advancedMethods.models import *


class TestProcessModel(TestCase):
    def test_model_fields(self):
        model = Process.objects.create(
            title="test",
            days_activation=1
        )
        self.assertEqual(model.title, "test")
        self.assertEqual(model.days_activation, 1)