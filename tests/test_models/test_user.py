#!/usr/bin/python3
"""
Tests for User Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test for User Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup User Class
        """
        cls.user = User()
        cls.user.email = "unit@test.com"
        cls.user.password = "invalid"
        cls.user.first_name = "Olivia"
        cls.user.last_name = "Dunan"

    @classmethod
    def teardown(cls):
        """
        Delete User Class
        """
        del cls.user
        try:
            os.remove("file.json")
        except:
            pass

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_attributes(self):
        """
        Check User attributes
        """
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        #self.assertEqual(type(self.user.name), str)

    def test_methods(self):
        """
        Check User and Basemodel methods
        """
        self.assertTrue(hasattr(User, "__init__"))
        self.assertTrue(hasattr(User, "__str__"))
        self.assertTrue(hasattr(User, "save"))
        self.assertTrue(hasattr(User, "to_dict"))

    def test_init(self):
        """
        Check object as instance of User
        """
        self.assertTrue(isinstance(self.user, User))

    def test_str(self):
        """
        Check string representation of User object
        """
        user_str = str(self.user)
        self.assertEqual(True, "[User] ({})".format(self.user.id) in user_str)
        self.assertEqual(True, "first_name" in user_str)
        self.assertEqual(True, "last_name" in user_str)
        self.assertEqual(True, "email" in user_str)
        self.assertEqual(True, "password" in user_str)
        self.assertEqual(True, "created_at" in user_str)
        self.assertEqual(True, "updated_at" in user_str)
        self.assertEqual(True, "datetime.datetime" in user_str)

    def test_save(self):
        """
        Check save method
        """
        self.user.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        user_dict = self.user.to_dict()
        self.assertEqual(self.user.__class__.__name__, 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(type(user_dict), dict)

if __name__ == "__main__":
    unittest.main()
