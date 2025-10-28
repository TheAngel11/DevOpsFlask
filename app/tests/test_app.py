import unittest
from src.main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Crear un cliente de testing
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Llamada GET a la ruta "/"
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_get_data(self):
        # Llamada GET a la ruta "/get_data"
        response = self.app.get('/get_data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Data ...')

if __name__ == '__main__':
    unittest.main()