import unittest
from application import *
import requests


class TestSite(unittest.TestCase):
    def test_calcam(self):
        self.assertEqual(calcam(-100, 1, 1, 1), 0)
        self.assertEqual(calcam(100, -1, 1, 1), 0)
        self.assertEqual(calcam(100, 1, -1, 1), 0)
        self.assertEqual(calcam(100, 1, 1, 3), 0)
        self.assertEqual(calcam(100, 1, 1, 5), 0)
        self.assertEqual(calcam(100, 1, 1, 6), 0)
        self.assertEqual(calcam(100, 1, 1, 7), 0)
        self.assertEqual(calcam(100, 1, 1, 8), 0)
        self.assertEqual(calcam(100, 1, 1, 9), 0)
        self.assertEqual(calcam(100, 1, 1, 10), 0)
        self.assertEqual(calcam(100, 1, 1, 11), 0)

        self.assertEqual(calcam(100, 10, 1, 1), 110)

    def test_calcin(self):
        self.assertEqual(calcin(-100, 100), 0)
        self.assertEqual(calcin(100, 0), 0)
        self.assertEqual(calcin(500, 974), 474)

    def test_site(self):
        page = requests.get('http://127.0.0.1:5000')
        self.assertEqual(page.status_code, 200)


