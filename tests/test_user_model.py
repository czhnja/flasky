import unittest
from app.models import User

class UserModelTestcase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'asdf')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'asdf')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'asdf')
        self.assertTrue(u.verify_passowrd('asdf'))
        self.assertFalse(u.verify_passowrd('catf'))

    def test_password_salts_are_random(self):
        u = User(password='asdf')
        u2 = User(password='asdf')
        self.assertTrue(u.password_hash != u2.password_hash)