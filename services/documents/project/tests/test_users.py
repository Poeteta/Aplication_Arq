# services/documents/project/tests/test_users.py

import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import User
from project.tests.utils import add_user


# class TestAppService(BaseTestCase):
     
#     # def test_add_user(self):
#     #     user = add_user('richi', 1, 'pacheco', 'daniel@gmail.com', 'daniel123', 1)
#     #     self.assertTrue(user.id)
#     #     self.assertEqual(user.username, 'richi')
#     #     self.assertEqual(user.entity_id, 1)
#     #     self.assertEqual(user.lastname, 'pacheco')
#     #     self.assertEqual(user.email, 'daniel@gmail.com')
#     #     self.assertEqual(user.password, 'daniel123')
#     #     self.assertEqual(user.status, 1)

    
    
# if __name__ == '__main__':
#     unittest.main()