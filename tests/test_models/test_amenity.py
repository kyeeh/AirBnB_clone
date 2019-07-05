#!/usr/bin/python3
"""
Tests for Amenity Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test for Amenity Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Amenity Class
        """
        cls.amt = Amenity()
        cls.amt.name = "Snaks"

    @classmethod
    def teardown(cls):
        """
        Delete Amenity Class
        """
        del cls.amt
        try:
            os.remove("file.json")
        except:
            pass

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_methods(self):
        """
        Check Amenity and Basemodel methods
        """
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(hasattr(Amenity, "save"))
        self.assertTrue(hasattr(Amenity, "to_dict"))

    def test_init(self):
        """
        Check object as instance of Amenity
        """
        self.assertTrue(isinstance(self.amt, Amenity))

    def test_str(self):
        """
        Check string representation of Amenity object
        """
        amt_str = str(self.amt)
        self.assertEqual(True, "[Amenity] ({})".format(self.amt.id) in amt_str)
        self.assertEqual(True, "name" in amt_str)
        self.assertEqual(True, "created_at" in amt_str)
        self.assertEqual(True, "updated_at" in amt_str)
        self.assertEqual(True, "datetime.datetime" in amt_str)

    def test_attr_types(self):
        """
        Check types defined
        """
        self.assertEqual(type(self.amt.name), str)

    def test_save(self):
        """
        Check save method
        """
        self.amt.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(self.amt.created_at, self.amt.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        amt_dict = self.amt.to_dict()
        self.assertEqual(self.amt.__class__.__name__, 'Amenity')
        self.assertIsInstance(amt_dict['created_at'], str)
        self.assertIsInstance(amt_dict['updated_at'], str)
        self.assertEqual(type(amt_dict), dict)

if __name__ == "__main__":
    unittest.main()
