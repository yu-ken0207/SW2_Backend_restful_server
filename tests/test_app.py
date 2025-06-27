import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_empty_name(self):
        response = self.client.post('/user', json={"name": "", "age": 30})
        self.assertEqual(response.status_code, 400)

    def test_age_999(self):
        response = self.client.post('/user', json={"name": "Test", "age": 999})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
