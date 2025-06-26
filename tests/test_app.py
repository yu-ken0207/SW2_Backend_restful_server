import unittest
from app_ori import app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_empty_name(self):
        response = self.client.post('/user', json={"name": "", "age": 30})
        self.assertEqual(response.status_code, 400)

    def test_age_999(self):
        response = self.client.post('/user', json={"name": "Test", "age": 999})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
