# services/documents/project/tests/test_users.py


import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import Document


class TestAppService(BaseTestCase):
    """Tests for the Users Service."""

    def test_app(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/documents/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


    def test_add_document(self):
        """Asegurar que un nuevo usuario puede ser agregado a la base de datos"""
        with self.client:
            response = self.client.post(
                '/documents',
                data=json.dumps({
                    'documentname': 'certificado de notas ingles',
                    'documentcode': 'ST001',
                    'documenttype': 'Certificado',
                    'documentprice': 19
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('Certificado agregado!', data['message'])
            self.assertIn('success', data['status'])

    
    
if __name__ == '__main__':
    unittest.main()