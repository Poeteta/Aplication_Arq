import json
import unittest


from project.tests.base import BaseTestCase
from project import db
from project.api.models import Entity
from project.tests.utils import add_entity


class TestAppService(BaseTestCase):
    def test_add_entity(self):
        entity = add_entity('Escuela de Arquitectura', 'FIA', 'E200')
        self.assertTrue(entity.id)
        self.assertEqual(entity.entityname, 'Escuela de Arquitectura')
        self.assertEqual(entity.entityplace, 'FIA')
        self.assertEqual(entity.entitycode, 'E200')


if __name__ == '__main__':
    unittest.main()
