import unittest
from api_server1 import app


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tester = app.test_client(cls)

    def test_index(self):
        response = self.tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_multiply(self):
        response = self.tester.get('/multi/10')
        self.assertEqual(response.json['result'], 10 * 10)


if __name__ == '__main__':
    unittest.main()
