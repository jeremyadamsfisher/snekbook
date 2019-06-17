from unittest import TestCase as UnitTestCase
from django.test import TestCase


class SnekbookTests(TestCase):
    def test_test(self):
        self.assertEqual(1, 1)
