# services/documents/project/tests/test_document.py

import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import Document
from project.tests.utils import add_document


class TestAppService(BaseTestCase):
     
    def test_add_document(self):
        document = add_document('Certificado de Estudios', 'C002', 'Certificado', 19)
        self.assertTrue(document.id)
        self.assertEqual(document.documentname, 'Certificado de Estudios')
        self.assertEqual(document.documentcode, 'C002')
        self.assertEqual(document.documenttype, 'Certificado')
        self.assertEqual(document.documentprice, 19)

    
    
if __name__ == '__main__':
    unittest.main()