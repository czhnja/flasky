import unittest
from app import create_app, db
from app.models import User
from app.auth.forms import RegistrationForm
from wtforms import ValidationError

class UserRegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_reg_email(self):
        u1 = User(email='abcd@abc.com',username='abcd',password='abcd')
        db.session.add(u1)
        regform = RegistrationForm()
        regform.email.data='abcd@abc.com'
        regform.username.data='abcd'
        regform.password.data='abcd'
        self.assertRaises(ValidationError,regform.validate_email(regform.email))

    def test_reg_username(self):
        u1 = User(email='abcd@abc.com',username='abcd',password='abcd')
        db.session.add(u1)
        regform = RegistrationForm()
        regform.email.data='abcd@abc.com'
        regform.username.data='abcd'
        regform.password.data='abcd'
        self.assertRaises(ValidationError,regform.validate_username(regform.username))